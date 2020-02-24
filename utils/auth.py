from flask import session, redirect
import functools
# 登录认证装饰器


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not session.get("userinfo", ""):
            return redirect("/login")
        res = func(*args, **kwargs)
        return res
    return inner
