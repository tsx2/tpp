from flask_restful import fields
from apps.main.models import Movies


# result = {
#     'status': '',
#     'msg': '',
#     'data': {
#         'movie': {
#             # 'hot_counts': 89,
#             # 'will_counts': 526,
#             'hot_movies': [],
#             'will_movies': []
#         }
#     }
# }

area_fields={
    'aid':fields.Integer,
    'partent_id':fields.Integer,

    }

normal_area={
    'first':fields.String,
    'normal_list':fields.Integer

}
movie_fields = {
    'mid': fields.Integer,
    'show_name': fields.String,
    'show_name_en': fields.String,
    'director': fields.String,
    'leading_role': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.String,
    'screening_model': fields.String,
    # 'open_day': fields.datetime.,
    'pic': fields.String,
    'flag': fields.Integer,
}

movies_fields = {
    'hot_count': fields.Integer,
    'will_count': fields.Integer,
    'hot_movies': fields.List(fields.Nested(movie_fields)),
    'will_movies': fields.List(fields.Nested(movie_fields))
}

data_fields = {
    'movie': fields.Nested(movies_fields)
}

result = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(data_fields)
}