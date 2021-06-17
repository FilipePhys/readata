from app_core.app_main import db
from sqlalchemy.ext.automap import automap_base


try:
    base = automap_base()
    base.prepare(db.engine,reflect=True)
    database_table = base.classes.users_customuser
    database_read = db.session.query(database_table).all()
except:
    # Criar um retorno aki!
    print("Database was not find!")


