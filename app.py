from flask import Flask

app = Flask(__name__)


# POST /store data: {name:}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item
# GET /store/<string:name>/item

app.run(port=5000)
