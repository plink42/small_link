from application.tests import client

def test_index(client):
    response = client.get('/')
    html = response.data.decode()
    assert response.status_code == 200
    assert '<input class="form-control" id="url" name="url" placeholder="Enter URL" required type="text" value="">' in html
    assert '<button type="submit" class="btn btn-dark">Shorten</button>' in html
    assert '<input id="csrf_token" name="csrf_token" type="hidden"' in html

def test_redirect(client):
    response = client.get('/MYTEST/')
    print(response.status_code)
    assert response.status_code == 301
    print(response.headers)
    print(response.location)
    assert response.headers['Location'] == 'https://fast.com'