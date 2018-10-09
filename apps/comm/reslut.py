from flask_restful import fields


class Result:
    # 第一种 data是列表类型
    # result = {
    #     'status': fields.Integer,
    #     'msg': fields.String,
    #     'data': fields.List()
    # }

    # @staticmethod
    # def get_success_result_list():
    #     return {
    #         'status': fields.Integer,
    #         'msg': fields.String,
    #         'data': fields.List
    #     }

    # 第二种 data是对象类型
    # result = {
    #     'status': fields.Integer,
    #     'msg': fields.String,
    #     'data': fields.Nested(data_fields)
    # }

    @staticmethod
    def get_success_result_obj(data=None, status=200, msg='success'):
        return {
            'status': status,
            'msg': msg,
            'data': data
        }

    @staticmethod
    def get_error_result(status=404, msg='error'):
        return {
            'status': status,
            'msg': msg
        }
