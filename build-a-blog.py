from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import html
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Blog(db.Model):

    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, name):
        self.title = title
        slef.body = body

@app.route('/')
def reroute():
    return redirect  ('/blog')


@app.route('/blog', methods=['GET','POST'])
def main():
    #title = title.query.filter_by(title).all()
    #body = body.query.filter_by(body).all()
    

    return render_template("main_form.html" )

    #if request.method="GET":
     #   for i in posts:
      #      print i
            






@app.route('/new_post', methods =  ["GET","POST"])
def entry():
    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']

        #if new_title == '':
            #need error return
        #if new_body=='':
            #need error return

        new_entry=Blog(new_title,new_body)
        db.session.add(new_entry)
        db.session.commit()

        posts=Blog.query.all()

        return render_template("/new_post",posts)
    else:
        return render_template("/entry_form.html")

if __name__ == '__main__':
    app.run()