#######################################################################################
# Author ： CHR_崔贺然
# Time ： 2020
# Description ： 项目配置文件
#######################################################################################



# https://www.cnblogs.com/GGGG-XXXX/articles/10182786.html
# 开发环境


class DevConfig(object):
    DEBUG = True
    SECRET_KEY = "chr"

# 生产环境


class ProConfig(object):
    DEBUG = False

# 测试环境


class TestConfig(object):
    TESTING = True
