from flask import Flask, request, render_template, abort
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


'''
    转换器有下面几种：
    -------|----------------------
    int	   |接受整数
    -------|----------------------
    float  |同 int ，但是接受浮点数
    -------|----------------------
    path   |和默认的相似，但也接受斜线
    -------|----------------------
'''


@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s ' % username


'''
    HTTP请求方法
'''


@app.route("/login", methods=['GET', 'POST'])
def login():
    # abort(404) # 指定404错误
    if request.method == "POST":
        return 'Request Method %s ' % 'POST'
    else:
        return 'Request Method %s' % 'GET'


'''
    模板渲染:默认路径放在templates目录下
'''


@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', username=username)


'''
    文件上传
'''

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')  # 获取flask-learning.py文件路径
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file1']
        # 这里以安全的形式上传文件,
        from werkzeug import secure_filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return '上传成功!!!'
    return render_template('upload.html')


'''
    错误页面:可以将所有错误信息都写到模板中。一劳永逸
'''


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
