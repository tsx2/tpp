from apps.ext import db


class Area(db.Model):
    aid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    parent_id = db.Column(db.Integer)
    short_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    merger_name = db.Column(db.String(64), nullable=False)
    level = db.Column(db.String(64), nullable=False)
    pinyin = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)
    zip_code = db.Column(db.String(64), nullable=False)
    first = db.Column(db.String(64), nullable=False)
    lng = db.Column(db.String(64), nullable=False)
    lat = db.Column(db.String(64), nullable=False)
    is_host=db.Column(db.Boolean,default=0)

class Movies(db.Model):
    mid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 电影中文名
    show_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    # 电影英文名称
    show_name_en = db.Column(db.String(64), nullable=False, index=True, unique=True)
    # 导演
    director = db.Column(db.String(32), nullable=False, index=True)
    # 主演
    leading_role = db.Column(db.String(256), nullable=False, index=True)
    # 影片类型
    type = db.Column(db.String(64), nullable=False)
    # 影片国家
    country = db.Column(db.String(32), nullable=False)
    # 语言
    language = db.Column(db.String(32), nullable=False)
    # 影片长度
    duration = db.Column(db.String(32), nullable=False)
    # 播放类型 IMAX 2D 3D 4D
    screening_model = db.Column(db.String(32), nullable=False)
    # 上映日期
    open_day = db.Column(db.Date)
    # 影片海报
    pic = db.Column(db.String(256), nullable=False)
    # 1即将上映 2 正在热映
    flag = db.Column(db.SmallInteger, default=1)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=1)
