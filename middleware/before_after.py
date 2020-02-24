# flask的中间件


class MiddleWare(object):
    def __init__(self, old_request):
        self.old_request = old_request

    def __call__(self, *args, **kwargs):

        print("before_process")
        res = self.old_request(*args, **kwargs)
        print("after_process")
        return res
