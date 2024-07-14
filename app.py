"""
http://127.0.0.1:5000/openapi/swagger
Only works with app.post and app.get and not with app.route
"""

from flask_openapi3 import OpenAPI

app = OpenAPI(__name__)


# @app.route('/book', methods=["GET"])
@app.get('/book')
def get_books():
    return ["book1", "book2"]


@app.post('/book')
def create_book():
    return {"message": "success"}


if __name__ == '__main__':
    app.run()