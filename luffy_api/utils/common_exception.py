from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from utils.common_response import APIResponse
from utils.common_logger import logger


# 自定义异常类
class PasswordException(Exception):
    pass


def exception_handler(exc, context):
    res = drf_exception_handler(exc, context)
    request = context.get("request")
    view = context.get("view")
    ip = request.META.get("REMOTE_ADDR")
    path = request.get_full_path()
    method = request.method
    user_id = request.user.id or "匿名用户"
    logger.error(
        f"操作出错!{str(exc)},视图类:{str(view)},ip:{ip},请求地址:{path},请求方式:{method},用户id:{user_id}"
    )

    if res:
        # drf异常
        if isinstance(res.data, dict):
            err = res.data.get("detail")
        elif isinstance(res.data, list):
            err = res.data[0]
        else:
            err = "服务异常，请稍后再尝试，[drf]"
            response = APIResponse(code=4000, msg=err)
    else:
        # 非drf异常
        if isinstance(exc, ZeroDivisionError):
            err = "数据操作出错,除以0了"
            code = 4001
        elif isinstance(exc, PasswordException):
            err = "密码错误!"
            code = 4002
        else:
            err = f"系统错误：{str(exc)}"
            code = 4004
        response = APIResponse(code=code, msg=err)
    return response
