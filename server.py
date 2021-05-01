from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('./templates/index.html')

@app.route('/about')
def about():
    return render_template('./templates/about.html')

@app.route('/blog')
def blog():
    return 'These on my thoughts on blogs'
    
@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'