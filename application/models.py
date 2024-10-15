'''Models for the application'''
import random
import string
from application import db

class Urls(db.Model):
    __tablename__ = 'urls'
    linkid = db.Column(db.String(6), primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    hits = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<Url {self.linkid}>'
    
    def create_link_id(self):
        '''Create a unique link id'''
        # Generate a random 6 character string with letters and digits
        # 36^6 = 2,176,782,336 possible combinations
        linkid = ''.join(random.choices(string.ascii_uppercase+ string.digits, k=6))
        # Check if the link id already exists
        while Urls.query.get(linkid):
            linkid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return linkid
    
    def add_url(self, url):
        '''Add a new URL to the database'''
        self.linkid = self.create_link_id()
        self.url = url
        return self.linkid
    
    def get_url(self, linkid):
        '''Get the URL from the database'''
        if self.url and self.active:
            self.hits += 1
            return self.url
        return None