from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'username': 'Jason',
        'now_time': datetime(2020, 10, 14, 21, 00, 0)
    }

    return render_template('customerTemplate.html', **context)


# Customer Template Filter
@app.template_filter('my_filter')
def my_filter(value):
    return value.replace('Jason', 'hi')


@app.template_filter('handle_time')
def handle_time(time):
    """
    小于一分鐘 --> 剛剛
    大于一分鐘 小于一小時 --> XXX分鐘之前
    大于一小時 小于24小時 --> XXX小時之前
    :param value:
    :return:
    """

    now = datetime.now()
    # 獲取總秒數
    time_stamp = (now - time).total_seconds()

    if isinstance(time, datetime):
        if time_stamp < 60:
            return '剛剛'
        elif 60 <= time_stamp <= 60 * 60:
            return '%s分鐘之前' % int(time_stamp / 60)
        elif 60 * 60 < time_stamp <= 60 * 60 * 24:
            return '%s小時之前' % int(time_stamp / (60 * 60))
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)
