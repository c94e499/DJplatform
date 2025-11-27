"""Set model for Mixcraft DJ Platform."""
from datetime import datetime
from app import db


class Set(db.Model):
    """Set model representing DJ sets/playlists."""
    __tablename__ = 'sets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    cover_url = db.Column(db.String(500))
    is_public = db.Column(db.Boolean, default=True)
    play_count = db.Column(db.Integer, default=0)
    like_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forked_from_id = db.Column(db.Integer, db.ForeignKey('sets.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    versions = db.relationship('SetVersion', backref='set', lazy='dynamic')
    forks = db.relationship('Set', backref=db.backref('forked_from', remote_side=[id]))

    def to_dict(self):
        """Convert set to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'cover_url': self.cover_url,
            'is_public': self.is_public,
            'play_count': self.play_count,
            'like_count': self.like_count,
            'user_id': self.user_id,
            'forked_from_id': self.forked_from_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Set {self.title}>'
