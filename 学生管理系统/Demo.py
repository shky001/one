# 导入flask类
from datetime import time

from flask import Flask, render_template, request, session, json, url_for
# 实例化flask对象
from werkzeug.utils import redirect

app = Flask(__name__)

# 学生信息
students = [
    {'id':'1','name':'哆啦A梦','age':18,'address':'运城市'},
    {'id':'2','name':'大耳朵图图','age':16,'address':'临汾市'},
    {'id':'3','name':'大头儿子','age':12,'address':'晋中市'},
    {'id':'4','name':'光头强','age':24,'address':'太原市'},
]
find = []
# new = [{'id':0,'name':'0','age':0,'address':'0'}]


# 定义视图和路由
@app.route('/')         # 访问的路径,使用route()装饰器告诉Flask应该触发我们的函数的URL
def hello_world():
    return '学生信息管理系统'



@app.route("/login",methods=("GET","POST"))
def login():
    print("00000",request.method)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 登陆成功，链接数据库，校验用户名+密码
        # 浏览器传递至服务器的登录信息
        print("从服务器所接受的数据：", username,password)
        # 登录成功后跳转至管理页面
        if username == 'admin' and password == '123456':
            return redirect('/admin')  # 重定向

    return render_template('login.html',msg='用户名或密码输入错误')    # 返回登录界面



@app.route('/admin')
def admin():
    # 将学生数据传递至管理页面中
    return render_template('admin.html',students = students )



@app.route('/query',methods=("GET","POST"))
def query():
    print("查询！！！！！！")
    if request.method == "POST":
        num = request.form.get('num')
        print("查询信息序号：", num)
        print("num 的类型： ",type(num))
        # Num = int(num)
        # print("查询完毕！！！！！！")
        for i in students:
            print(i["id"] == num)
            print("i[id]的类型",type(i["id"]))
            if i["id"] == num:
                find = i
                print(find)
                # print(find['id'],find['name'],find['age'])
                return render_template('query.html', find=find)
            else:
                return '没有您要找的学号'
        # return redirect("/stu_query")

    return render_template("query.html")          # 返回添加界面



@app.route('/add',methods=("GET","POST"))
def add():
    print("添加添加添加！！！！！！")
    if request.method == "POST":
        # print("下一步为返回添加页面")
        id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        print("新增学员信息：", id, name, age, address)
        students.append({'id': id, 'name': name, 'age': age, 'address': address})
        print("添加完毕！！！！！！")
        # print(students[0])
        # print(students[4])
        return redirect("/admin")

    return render_template("add.html")          # 返回添加界面



@app.route('/delete')
def delete():
    print(request.method)
    ID = request.args.get('id')
    # INT_ID = int(ID)
    print(request.args.get('id'))
    for stu in students:
        print(stu['id'],ID)
        print("类型：：：：：：",type(stu['id']),type(ID))
        print(stu['id'] == ID)
        print("*************************")
        if stu['id'] == ID:
            students.remove(stu)
            print("删除成功！")
        # elif type(stu['id']) == 'str':
        #     print("222222222222222222222222")
        #     if stu['id'] == ID:
        #         students.remove(stu)
        #         print("删除成功！！")

    return redirect('/admin')



@app.route('/exit')
def exit():
    return render_template('exit.html')



# 服务器启动了，程序入口包一下
if __name__ == '__main__':
    app.run()           # Flask类的run()方法在本地开发服务器上运行应用程序

# if __name__ == '__main__':
#     app.run(debug=True)

# if __name__ == '__main__':
#
#     from gevent import pywsgi
#
#     server = pywsgi.WSGIServer(('0.0.0.0',5000),app)
#     server.serve_forever()
