from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, HiddenField
from flask_pagedown.fields import PageDownField
from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField('Username*', [validators.InputRequired("Please enter your name.")])
    password = PasswordField('Password*', [validators.InputRequired("Please enter your password.")])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    username = StringField('Username*', [validators.InputRequired("Please enter your username")])
    email = StringField('Email*', [validators.InputRequired("Please enter your email"), validators.Email('Email format incorrect')])
    password = PasswordField('Password*', [validators.InputRequired("Please enter your password"), validators.EqualTo('confirm_password', message='Passwords must match'), validators.Length(min=8, max=32, message='Password must contain 8 digits minimum, with 32 being maximum')])
    confirm_password = PasswordField('Confirm your password*', [validators.InputRequired("Confirm your password")])
    submit = SubmitField('Signup')

class AddNoteForm(FlaskForm):
    note_id = HiddenField("Note ID:")
    note_title = StringField('Note Title:', [validators.InputRequired("Please enter a note title.")])
    note = PageDownField('Your Note:')
    tags = SelectMultipleField('Note Tags:')
    submit = SubmitField('Add Note')

class AddTagForm(FlaskForm):
    tag = StringField('Enter tag:', [validators.InputRequired("Please enter the tag")])
    submit = SubmitField('Add Tag')

class ChangeEmailForm(FlaskForm):
    email = StringField('Email*', [validators.InputRequired("Please enter our email"), validators.Email('Email format incorrect')])
    submit = SubmitField('Update Email')

class ChangePasswordForm(FlaskForm):
    password = PasswordField('Set new password*', [validators.InputRequired("Please enter your password"), validators.EqualTo('confirm_password', message='Passwords must match'), validators.Length(min=8, max=32, message='Password must contain 8 digits minimum, with 32 being maximum')])
    confirm_password = PasswordField('Confirm new password*', [validators.InputRequired("Confirm your password")])
    submit = SubmitField('Update Password')
