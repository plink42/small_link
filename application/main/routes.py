from flask import render_template, request, Blueprint, redirect, current_app
from application.models import Urls
from application.main.forms import ShortenForm
from application import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ShortenForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            url = form.url.data
            link = Urls()
            linkid = link.add_url(url)
            db.session.add(link)
            db.session.commit()
            return render_template('main/index.html', 
                                   form=form, 
                                   title='Smallify Your URL', 
                                   linkid=linkid)
        else:
            return render_template('main/index.html', 
                                   form=form, 
                                   title='Smallify Your URL')
    return render_template('main/index.html', 
                           form=form, 
                           title='Smallify Your URL')

@main.route('/<linkid>/')
def forward(linkid):
    url = Urls.query.get(linkid)
    if url:
        u = url.get_url(linkid)
        return redirect(u, code=301)
    else:
        return render_template('main/404.html', title='404 Not Found'), 404
