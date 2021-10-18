# import flask
import flask_wtf
import wtforms
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired


class LoginForm(flask_wtf.FlaskForm):
    """
    A class used to represent a login form.
    """

    # class attributes
    # ...

    # --- for email field
    email_data_required_validator_instance = wtforms.validators.data_required()
    email_validator_instance = wtforms.validators.email()
    email_address = wtforms.StringField(label=u'Email Address', validators=[
        email_data_required_validator_instance,
        email_validator_instance,
    ])

    # --- for password field
    password_data_required_validator_instance = wtforms.validators.data_required()
    password_validator_instance = wtforms.validators.length(min=8)
    password = wtforms.PasswordField(label=u'Password', validators=[
        password_data_required_validator_instance,
        password_validator_instance,
    ])

    # --- for submit button
    log_in_button = wtforms.SubmitField(
        label=u'Log In',
    )
