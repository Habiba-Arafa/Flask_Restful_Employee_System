from flask import Flask , jsonify
from routes.routes import routes


app = Flask(__name__)

app.register_blueprint(routes)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"message":"Resource not found"}),404 

if __name__ == "__main__" :
    app.run(debug=True)



