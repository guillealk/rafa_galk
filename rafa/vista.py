#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for
import proyecto
from flask import render_template

app = Flask(__name__)


# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Project 1</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Project 1</h1>
    <form method=post>
      <div><button id="go" type="submit">What are the most popular three articles of all time? </button></div> <br>
      <div><button id="go" type="submit">Who are the most popular article authors of all time?</button></div> <br>
      <div><button id="go" type="submit">On which days did more than 1% of requests lead to errors? </button></div> <br>
    </form>
    <!-- post content will go here -->

  </body>
</html>
'''

HTML_VISTA1 = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Project 1</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
  <tbody>
    {% for i in range(10) %}
        <tr>
          <td>{{ "eaeas" }}</td>
          <td>{{ "dsadas" }}</td>
        </tr>
    {% endfor %}
  </tbody>
  </body>
</html>
'''

@app.route('/')
def main():
  '''Main page of the forum.'''
  
  return HTML_WRAP

@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  
  return render_template('views.html', data=proyecto.datos1())

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True, port=8001)

