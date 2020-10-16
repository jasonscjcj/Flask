## Flask

#### Day 1

##### 安裝

```
pip install pipenv
```

##### 創建虛擬環境

```
pipenv shell	# 進入虛擬環境

pip install flask	# 在shell入面安裝flask

pip list	# 查看安裝了什麼

pipenv install --dev 框架名字	#記錄安裝了什麼到Pipfile

exit	# 離開虛擬環境

pipenv --rm	# 刪除虛擬環境，但不會刪除pipfile

```

##### pipenv command

```
$ pipenv Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Options: 
--where 顯示項目文件所在路徑
--venv 顯示虛擬環境實際文件所在路徑
--py 顯示虛擬環境Python解釋器所在路徑
--envs 顯示虛擬環境的選項變量
--rm 刪除虛擬環境
--bare 最小化輸出
--completion 完整輸出
--man 顯示幫助頁面
--three / --two 使用Python 3/2創建虛擬環境（注意本機已安裝的Python版本） 
--python TEXT 指定某個Python版本作為虛擬環境的安裝源
--site-packages 附帶安裝原Python解釋器中的第三方庫
--jumbotron An easter egg, effectively. 
--version 版本信息
-h, --help 幫助信息
```

##### Pipfile

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple" #指定pip源
verify_ssl = true

[dev-packages]	# 開發環境

[packages]	# 生產環境

[requires]	# Python版本
python_version = "3.8"
```

##### Debug Mode
###### 方法1

```python
app.debug = True
app.run()
```
###### 方法2

```python
app.run(debug=True)
```
###### 方法3

```python
app.config.update(DEBUG=True)
app.config.update({'DEBUG' : True})
app.config['DEBUG'] = True
app.config.update(DEBUG = True, SECRECT_KEY = xxxxx)
```
###### 方法4

```python
# 使用自定義config file，需要import config
# 4.1 通過模組字串
app.config.from_object(config)
# 4.2 通過模組物件
import config
app.config.from_object('config')
# 4.3
app.config.from_pyfile('config.py', silent=True)
# 4.4
app.config.from_pyfile('config.ini', silent=True)
```

開啟了Debug Mode的畫面

```
* Serving Flask app "firstFlask" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 202-551-615
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

#### Day 2

##### URL 與 視圖

```python
/ 分隔符
? 分隔符
函數和URL的映射關系
string : 默認的資料類型，接受沒有任何斜杠/的字串
int: 整形
float: 浮點型。
path： 和string類似，但是可以傳遞斜杠/。
uuid： uuid類型的字串。any：可以指定多種路徑

http://127.0.0.1:5000/list/1234
@app.route('/list/<int:sid>')
def article(sid):
    return '這是第{}篇文章, uuid : {}' \
        .format(sid, uuid.uuid4())
        

http://127.0.0.1:5000/dict/
http://127.0.0.1:5000/tuple/
@app.route('/<any(dict,tuple):url_path>/')
def item(url_path):
    return url_path

from flask import Flask, request

http://127.0.0.1:5000/ie?name=python
@app.route('/ie')
def baidu():
    return request.args.get('name')

http://127.0.0.1:5000/ie?name=python&last=abc
@app.route('/ie')
def baidu():
    return '{}{}'.format(request.args.get('name'), request.args.get('last'))

```

##### URL For

- 進行反轉，把函數名字轉化成URL

```
url_for('函數名字', 參數1, 參數2)
如困參數2不存在，會以?參數2的形式呈現
```

###### 好處

- url_for會進行轉碼

- 修改了URL地址，對我們的代碼影响不大，比硬編碼方式更靈活

###### URL末尾的反斜綫
- 有無反斜綫是兩個URL地址

###### 指定HTTP方法
```python
@app.route('xxx', methods=['請求方法'])

GET方法
request.args.get('xxx')

POST方法
request.from.get('xxx')
```

```python
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    print(url_for('article', aid=1)) # /article/1
    print(url_for('article', aid=1, page=1)) # /article/1?page=1
    print(url_for('article', aid=1, page=1, name=1))  # /article/1?page=1&name=1
    print(url_for('article', aid=1, page=1, name=1, type=1))  # /article/1?page=1&name=1&type=1
    return 'Hello World!!!'


@app.route('/article/<aid>')
def article(aid):
    return 'article list {}'.format(aid)


if __name__ == '__main__':
    app.run(debug=True)

```
##### 重定向 redirect
```
301 永久重定向
302 臨時重定向
return redirect(url_for('函數名', code=200))
```

```python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/login')
def login():
    return 'login'


@app.route('/profile/')
def profile():
    name = request.args.get('name')
    if name:
        return name
    else:
        return redirect(url_for('login'), code=301)


if __name__ == '__main__':
    app.run(debug=True)
```

##### Flask Template

```python
from flask import Flask, render_template

# template_folder盡量不要修改
app = Flask(__name__, template_folder = 'template')


@app.route('/')
def home():
    return render_template('ui/index.html')


if __name__ == '__main__':
    app.run(debug=True)
```

##### Response 響應
- 字符串
	return '字符串'
- 元組
	return ('','') OR return '',
- 字典
	return {'key','value'}
- Response
	reutrn Response(字符串, status=狀態碼, mimetype='text/html')
- make_response
	return make_response('字符串')

##### Template
###### 模板渲染
先創建一個目錄 templates, 將模板文件放到templates中
```
# template_folder盡量不要修改
# app = Flask(__name__, template_folder = 'template')

return render_template('模板文件名字')
```

###### 模板轉參
```
1. 方法 1
return render_template('index.html', username='jason')
在index.html中接收 {{username}}


2. 方法 2
context = {
	'key':'value'
}
return render_template('index.html', context=context)
在index.html中接收
- {{context.key}}
- {{context[key]}}

return render_template('index.html', **context)
在index.html中接收
- {{key}}
```

#### Day 3

##### 模版過濾器

###### 內置過濾器函數

 - abs
 - default
 - last
 - first
 - upper
 - lower
 - escape
 - safe
 - length
 - replace
 - format
 - join
 - int
 - float
 - string
 - wordcount
 - truncate
 - striptags
 - trim

Template_filter.py
```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'username': 'Jason',
        'age': -18,
        'home': 'Hong Kong',
        'name': 'logic',
        'es': "<script>alert('hello');</script>",  # escape
        'books': ['Python', 'Java', 'PHP'],
        'book': {'Python': 666},
        'tc': 'Hello Jason'
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

```

index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>首頁</h1>
    <p>{{username}}</p>
    <p>{{age|abs}}</p> <!-- abs = 絕對值 -->
    <p>{{name|default('這個人很懶，什麼都沒有留下')}}</p> <!-- default = 如果name不存在，則會使⽤函數內的字符串來替代 -->

    <!-- 關閉轉義 -->
    {% autoescape off %}
    <p>{{es}}</p>
    {% endautoescape %}
    <p>{{es}}</p> <!-- 變為字符串 -->
    <p>{{es|safe}}</p> <!-- 如果開了全局轉義，關閉轉義-->

    <p>{{books|first}}</p> <!-- 返回列表第一個元素-->
    <p>{{books|last}}</p> <!-- 返回列表最後一個元素-->
    <p>{{books|length}}</p> <!-- 返回列表總長度-->
    <p>{{books|first|length}}</p> <!-- 返回列表第一個總長度-->
    <p>{{book|length}}</p> <!-- 返回字典總長度-->

    <p>{{username|replace('Jason', 'jess')}}</p>
    <p>{{tc|truncate(length=5)}}</p>
    <p>{{es|striptags}}</p> <!-- Delete HTML Tag -->
    <p>{{tc|wordcount}}</p> <!-- 計算單字總數 -->
</body>
</html>
```

##### 自定義模版過濾器

```
@app.template_filter('自定義過濾器名字')
```

Template_filter.py
```python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'username': 'Jason',
        'now_time': datetime(2020, 10, 14, 21, 00, 0)
    }

    return render_template('index.html', **context)


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
        elif 60*60 < time_stamp <= 60*60*24:
            return '%s小時之前' % int(time_stamp/(60*60))
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)

```


index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>首頁</h1>
    <!-- Customer Template Filter -->
    <p>{{username|my_filter}}</p>
    <!-- Customer Time Template Filter -->
    <p>發表時間︰{{now_time|handle_time}}</p>
</body>
</html>

```

##### if for
- if

  ```
  {% if 判斷條件 %}
  {% elif %}
  {% else %}
  {% endif %}
  ```

- for
  
  ```
  {% for xx in xxx %}
  {% endfor %}
  ```

  獲取循環狀態
  
  ```
  loop.index 從1開始的索引
  loop.index0 從0開始的索引
  loop.first
  loop.last
  ```

if_for.py

```python
from flask import Flask, render_template

app = Flask(__name__)

context = {
    'username': 'Jasossn',
    'age': 18,
    'books': ['Python', 'Java', 'PHP'],
    'book': {'Python': 666, 'Java': 777, 'PHP': 888}
}


@app.route('/')
def if_for():
    return render_template('if_for.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

```


if_for.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>if for</h1>

<p>=====Start String=====</p>
{% if username == 'Jason' %}
<p>{{username}}</p>
{% else %}
<p>當前用戶不是{{username}}</p>
{% endif %}
<p>=====End String=====</p>

<p>=====Start List=====</p>
{% for book in books %}
<p>{{book}}</p>
{% endfor %}
<p>=====End List=====</p>


<p>=====Start Dist=====</p>

{% for b in book %}
<p>{{b}}</p>
{% endfor %}

{% for (key,value) in book.items() %}
<p>{{key}}</p>
<p>{{value}}</p>
{% endfor %}

{% for (key,value) in book.items() %}
<p>{{key}}</p>
<p>{{value}}</p>
<hr>
{% endfor %}

<p>=====End Dist=====</p>

<!--    loop.index 當前迭代的索引（從1開始）
    loop.index0 當前迭代的索引（從0開始）
    loop.first 是否是第⼀次迭代，返回True或False
    loop.last 是否是最後⼀次迭代，返回True或False
    loop.length 序列的⻓度-->

{% for book in books%}
<p>{{loop.index}} {{book}}</p>
{% endfor %}


</body>
</html>
```

##### macro

  - macro

  ```
  {% macro 名字(參數) %}
  # macro body
  {% endmacro %}
  ```

macro.py
```python
from flask import Flask, render_template

app = Flask(__name__)
context = {
    'username': 'Jason',
    'age': -18,
    'home': 'Hong Kong',
    'name': 'logic',
    'es': "<script>alert('hello');</script>",  # escape
    'books': ['Python', 'Java', 'PHP'],
    'book': {'Python': 666},
    'tc': 'Hello Jason',
}

@app.route('/')
def macro():
    return render_template('macro.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

```

macro.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>macro</h1>
    {% macro input(name, value='', type='text') %}
    <input type="{{type}}" , name="{{username}}" , value="{{value}}">
    {% endmacro %}

    <table>
        <tr>
            <td>用戶名</td>
            <td>{{input('username')}}</td>
        </tr>
        <tr>
            <td>密碼</td>
            <td>{{input('password', type='password') }}</td>
        </tr>
    </table>
</body>
</html>
```

##### import

  ```
  {% import 'xxx.html' as xxx %}
  
  {% from 'xxx.html' import macro名字 %}
  {% from 'xxx.html' input macro名字 as xxx %}
  
  {% from 'xxx.html' as xxx with context%}
  ```

other.html
```html
{% import 'macro.html' as macro  %} 
{% import 'macro.html' as macro  with context %} <!-- 包括參數 -->
{% from 'macro.html' import input %} <!-- import 其中的組件 -->
<body>
<!-- {% import 'macro.html' as macro  %} -->
<p>用戶名︰{{ macro.input('username') }}</p>
<!-- {% from 'macro.html' import input %} -->
<p>密碼︰{{input('password', type='password')}}</p>

</body>

```

