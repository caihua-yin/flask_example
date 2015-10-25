from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!\n"

@app.route("/user/<name>")
def user(name):
    return "Hello %s!\n" % name

@app.route("/post/<int:id>")
def get_post_id(id):
    return "The post ID is: %d\n" % id

if __name__ == "__main__":
    app.run()
