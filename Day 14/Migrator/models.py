from middleware import db


class User(db.Model):
    # __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))


article_tag_table = db.Table(
    'article_tag',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Article(db.Model):
    # __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(50))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref='articles')

    tags = db.relationship('Tag', secondary=article_tag_table,backref='tags')


class Tag(db.Model):
    # __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
