from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/members")
def members():
    # response = jsonify({"members": ["member1", "member2", "member3"]})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    return {"members": ["member1", "member2", "member3"]}
if __name__ == "__main__":
    app.run(debug=True)