from application.tests import app
from application.models import Urls

def test_get(app):
    app.app_context().push()
    url = Urls.query.filter(Urls.linkid == 'MYTEST').first()
    assert url.linkid == 'MYTEST'
    assert url.url == 'https://fast.com'
    assert url.hits == 24
    assert url.active == True