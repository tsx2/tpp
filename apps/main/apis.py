from operator import and_
from flask_restful import Resource, marshal_with

from apps.comm.reslut import Result
from apps.main.fields import result
from apps.main.models import Movies, Area

#根据字母查询城市
keys='ABCDEFGHIJKLMNOPQRESTUVWXYZ'

class HomeApi(Resource):
    @marshal_with(result)
    def get(self):
        #获取区域数据
        hot_areas=Area.query.with_entities(Area.aid,Area.short_name).filter()
        #根据首字母查询城市
        normal_areas=[{'A':[]}]
        for key in keys:
            normal_areas.append(key:Area.query.filter==key)
        #获取热门电影数据
        hot_count=Movies.query.filter(and_(Movies.flag==1,Movies.is_delete==0)).count()
        will_count = Movies.query.filter(and_(Movies.flag == 2, Movies.is_delete == 0)).count()
        hot_movies = Movies.query.filter(and_(Movies.flag == 1, Movies.is_delete == 0)).limit(5).offset(0).all()
        will_movies = Movies.query.filter(and_(Movies.flag == 2, Movies.is_delete == 0)).limit(5).offset(0).all()
        data={
            'movies':{
                'hot_count': hot_count,
                'will_count': will_count,
                'hot_MOVIES': hot_movies,
                'will_movies': will_movies,
            }

        }
        return Result.get_success_result_obj(data)

    def post(self):
        pass