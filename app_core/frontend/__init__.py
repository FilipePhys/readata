from .pages import bp_fe


def init_app(app):
    app.register_blueprint(bp_fe)