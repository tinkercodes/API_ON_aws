from flask_blog_app import app,db
from flask import jsonify,request,make_response,redirect,url_for,render_template
from flask_blog_app.models import Blog,User

@app.route('/')
def home():
    b_list = []
    for blog in Blog.query.all():
        b_list.append({
        'blog_id':blog.blog_id,
        'title':blog.title,
        'content':blog.content,
        'created_on':blog.created_on,
        'user':User.query.get(blog.u_id).user_name
        })
    return jsonify(b_list)

@app.route('/get_blog/<blog_id>',methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get(blog_id)
    data = {
        'blog_id':blog.blog_id,
        'title':blog.title,
        'content':blog.content,
        'created_on':blog.created_on,
        'user':User.query.get(blog.u_id).user_name
    }
    return jsonify(data)

@app.route('/post_blog',methods=['GET','POST'])
def post_blog():
    if(request.method=='GET'):
        return render_template('post_blog.html',blog={})
    form = request.form
    b1 = Blog(title=form.get('title'),content=form.get('content'),u_id=1)
    db.session.add(b1)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/delete_blog/<blog_id>',methods=['GET','DELETE'])
def delete_blog(blog_id):
    b1 = Blog.query.get(blog_id)
    db.session.delete(b1)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update_blog/<blog_id>',methods=['GET','PATCH','POST'])
def update_blog(blog_id):
    if(request.method=='GET'):
        blog = Blog.query.get(blog_id)
        blog = {
        'blog_id':blog.blog_id,
        'title':blog.title,
        'content':blog.content,
        'created_on':blog.created_on,
        'user':User.query.get(blog.u_id).user_name
        }
        return render_template('post_blog.html',blog=blog)
    form = request.form
    blog = Blog.query.get(blog_id)
    blog.title = form.get('title')
    blog.content = form.get('content')
    db.session.commit()

    return redirect(url_for('home'))


