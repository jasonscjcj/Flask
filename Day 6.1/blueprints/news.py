from flask import Blueprint

# name = 跟由名稱
news_bp = Blueprint(name='news', import_name=__name__)


@news_bp.route('/news/')
def book():
    return '這是新聞首頁'
