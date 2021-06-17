import pytest
from flask import url_for, request


def test_index(client):
    assert client.get(url_for('frontend.index')).status_code == 200


def test_request_headers(client):
    client.get(url_for('frontend.index'), headers=[('X-Something', '42')])
    assert request.headers['X-Something'] == '42'


@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app is not in debug mode'
