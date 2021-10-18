# from flask import Flask, render_template
import flask
import login_form
import flask_bootstrap

# app = flask.Flask(__name__)
app = flask.Flask(__name__)
flask_bootstrap.Bootstrap(app)
# app secret key
app.secret_key = 'enter secret key'


@app.route("/")
def home():
    return flask.render_template('./index.html')


@app.route("/login", methods=['GET', 'POST', ])
def login():
    form = login_form.LoginForm()
    if form.validate_on_submit():
        if form.email_address.data == 'admin@email.com' and form.password.data == '12345678':
            return flask.render_template('./success.html')
        else:
            return flask.render_template(template_name_or_list='./denied.html')
    return flask.render_template('./login.html', login_form=form)


if __name__ == '__main__':
    app.run(debug=True)
