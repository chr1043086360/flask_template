#######################################################################################
# Author ： CHR_崔贺然
# Time ： 2020
# TODO ： Flask项目搭建
# *
# !
# ?
#######################################################################################
from flask import Flask, render_template, request, redirect, url_for, session
from middleware.before_after import MiddleWare
from utils.auth import auth

from project import create_app

app = create_app()


# 获取项目环境
app.config.from_object("project.settings.DevConfig")

# 中间件注意这么写的技巧
app.wsgi_app = MiddleWare(app.wsgi_app)

#######################################################################################
# Param Data ：
# Return ：
# TODO ： 项目启动就会检查路径,但是静态文件会受影响,还是要用中间件做
# * : 重要的中间件[before_request, after_request, errorhandler(404)]
# * : 注意中间件有返回值时的流程, Flask是一直都走完,Django2.0之后只要有返回下面的就不走了
# !
# ?
#######################################################################################
# @app.before_request
# def auth():
#     # !这里的静态文件也会重定向
#     if request.path == "/login" or request.path == "/":
#         return None
#     # *虽然可以这么解决但是不好
#     elif request.path.startswith("/static"):
#         return None
#     elif not session.get("userinfo"):
#         return redirect("/login")
#     return None


@app.route("/index")
def default_index():
    return redirect("/")


#######################################################################################
# Param Data ： endpoint{命名路由,默认是函数的名字}
# Return ：set_cookie等操作
# TODO ： 首页
#######################################################################################
@app.route("/", endpoint="index")
@auth
def index():
    print(session.get("userinfo"))
    return "首页"

#######################################################################################
# Param Data ：
# Return ：
# TODO ： 登录接口,写入session
#######################################################################################
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")

        if username == "chr":
            # *flask内部是md5加盐需要自己指定
            session["userinfo"] = {"name": username}

            # 可以使用index就可以跳转
            return redirect(url_for("index"))
            # return redirect(url_for("book", nid=1))

    # *在模板语言中可以通过上下文信息获取到参数
    # login_list = [
    #     {"code": 200, "msg": "ok", "data": "chr"}
    # ]
    return render_template("login.html")


#######################################################################################
# Param Data : nid{路径传入参数,例:/book/1}
# Return ： string
# TODO ： 解析路径参数,默认支持路径参数
# {
# "string","default","any","path","int","float","uuid"
# }
#######################################################################################
@app.route("/book/<int:nid>", endpoint="book")
@auth
def book(nid):
    return "BookView"


#######################################################################################
# Param Data ：
# Return ：
# ? ： 我想单独再写一个文件里怎么弄, 不想耦合在一起
#######################################################################################
@app.errorhandler(404)
def page_not_found(error):
    return "页面找不到了"


# 启动项目主函数
if __name__ == '__main__':
    app.run()
