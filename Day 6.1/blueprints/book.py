from flask import Blueprint, render_template

# name = 路由名稱
# url_prefix = http://127.0.0.1/book
book_bp = Blueprint(
    name='book',
    import_name=__name__,
    url_prefix='/book',
    template_folder='logic',
    static_folder='lgcode')


# http://127.0.0.1:5000/book/
@book_bp.route('/')
def book():
    return render_template('book.html')


# http://127.0.0.1:5000/book/detail/2
@book_bp.route('/detail/<bid>')
def book_detail(bid):
    return '這是圖書第%s頁' % bid
