from app import app


@app.errorhandler(404)
def page_not_found(error):
    return "页面找不到了"
