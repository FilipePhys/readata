from flask import Blueprint, render_template


bp_fe = Blueprint('frontend', __name__)

@bp_fe.route('/index')
@bp_fe.route('/')
def index():
    return render_template('index.html')
