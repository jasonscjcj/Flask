from flask import g


# 沒使用g對象
# def log_a(username):
#     print('log a %s' % username)
#
#
# def log_b(username):
#     print('log b %s' % username)

# 使用g對象
def log_a():
    print('g log a %s' % g.username)


def log_b():
    print('g log b %s' % g.username)
