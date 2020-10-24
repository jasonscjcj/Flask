from flask import Blueprint

cms_bp = Blueprint('cms', __name__, subdomain='cms')


@cms_bp.route('/')
def cms():
    return 'cms頁面'
