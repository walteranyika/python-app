from flask import Flask,render_template,jsonify
from playhouse.shortcuts import  model_to_dict,dict_to_model
from  app_forms import MyForm
from  user_model import  User
from  peewee import OperationalError
app = Flask(__name__)
app.secret_key ="super_sceret_sdhwonpzmposiuswomsm7220as"

@app.route('/', methods=("GET","POST"))
def index():
    form = MyForm()
    if form.validate_on_submit():
        #everything is ok
        names = form.names.data
        email = form.email.data
        age = form.age.data
        password = form.password.data
        print("Names {0} Email {1} Age {2}".format(names,email,age))
        User.create(names=names, email=email, age=age, password=password)
        user =User.get(User.id==1)

    return render_template("index.html",form=form )


if __name__ == '__main__':
    try:
       User.create_table()
    except OperationalError:
        pass
    app.run()













