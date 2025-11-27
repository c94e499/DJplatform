"""Track model for Mixcraft DJ Platform."""
from datetime import datetime
from app import db


class Track(db.Model):
    """Track model representing music tracks."""
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200))
    album = db.Column(db.String(200))
    duration = db.Column(db.Integer)  # Duration in seconds
    bpm = db.Column(db.Float)
    key = db.Column(db.String(10))  # Musical key (e.g., "Am", "C#m")
    genre = db.Column(db.String(100))
    file_url = db.Column(db.String(500))
    waveform_url = db.Column(db.String(500))
    cover_url = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convert track to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'duration': self.duration,
            'bpm': self.bpm,
            'key': self.key,
            'genre': self.genre,
            'file_url': self.file_url,
            'waveform_url': self.waveform_url,
            'cover_url': self.cover_url,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Track {self.title}>'
