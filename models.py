from app import db, marshmallow

class Tune(db.Model):
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)