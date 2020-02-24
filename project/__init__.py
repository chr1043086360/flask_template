#######################################################################################
# Author ： CHR_崔贺然
# Time ： 2020
# TODO ： 初始化app并在main中导入run起来
#######################################################################################
from flask import Flask
from apis.user import userBlue
from apis.book import bookBlue


def create_app():

    # !可以添加配置信息static,templates,注意因为放在project文件夹中不是项目的跟路径,需要更改静态文件夹的路径
    # 前后端分离项目和后端渲染项目这里有区别, 因为会向/static,/templates文件夹请求资源
    app = Flask(__name__, template_folder="../templates/",
                static_folder="../static/")

    # *分组路由,相当于django中的主urls,gin中的分组路由
    app.register_blueprint(userBlue, url_prefix="/api/user")  # !必须以"/"开头
    app.register_blueprint(bookBlue, url_prefix="/api/book")

    return app
