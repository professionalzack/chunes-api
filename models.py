from app import db, marshmallow

tags = db.Table('tags',
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
  db.Column('tune_id', db.Integer, db.ForeignKey('tune.id'), primary_key=True)
)

class Tune(db.Model):
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)

  title = db.Column(db.String(100))
  time_signature = db.Column(db.String(10), default='4/4')
  default_note_length = db.Column(db.String(10), default='1/8')
  tune_type = db.Column(db.String(50))
  key_signature = db.Column(db.String(50))
  additional_info = db.Column(db.Text, nullable=True)
  
  poster = ForeignKeyField(User, related_name='tune_set')
  fork = relationship'Tune', backref=backref('tune_dad', remote_side=[id]), nullable=True)
  tags = db.relationship('Tag', secondary=tags, lazy='subquery',
    backref=db.backref('tunes', lazy=True), nullable=True)
  is_public = db.Column(db.Boolean(), default=False)

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), unique=True)
