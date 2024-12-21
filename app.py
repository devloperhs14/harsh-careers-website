# import libs
from flask import Flask, render_template

# create a app class from Flask

# name variable refers to how a praticular script is called/invoked - changes depending on where its invoked
app = Flask(__name__)

# add a route - url/route
@app.route('/') # decorator
def hello_world():
  return render_template('home.html')

# auto run
if __name__ == '__main__':
  app.run(host = "0.0.0.0", debug=True)