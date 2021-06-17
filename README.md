# readata
## read a database

______________________________________
P.S. If installed by requirements.txt:

go to 

.venv/lib/python3.8/site-packages/flask_restplus/fields.py"

.venv/lib/python3.8/site-packages/flask_restplus/api.py

change 

from werkzeug import cached_property, to

from werkzeug.utils import cached_property

and, in .venv/lib/python3.8/site-packages/flask_restplus/api.py

change 

from flask.helpers import _endpoint_from_view_func to

from flask.scaffold import _endpoint_from_view_func