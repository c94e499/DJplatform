"""Transition model for Mixcraft DJ Platform."""
from datetime import datetime
from app import db


class Transition(db.Model):
    """Transition model representing transitions between tracks."""
    __tablename__ = 'transitions'

    id = db.Column(db.Integer, primary_key=True)
    from_track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    to_track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    set_version_id = db.Column(db.Integer, db.ForeignKey('set_versions.id'), nullable=False)
    transition_type = db.Column(db.String(50))  # e.g., "crossfade", "cut", "echo"
    duration = db.Column(db.Integer)  # Duration in milliseconds
    start_position = db.Column(db.Integer)  # Start position in ms for from_track
    end_position = db.Column(db.Integer)  # End position in ms for to_track
    parameters = db.Column(db.JSON)  # Additional transition parameters
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    from_track = db.relationship('Track', foreign_keys=[from_track_id])
    to_track = db.relationship('Track', foreign_keys=[to_track_id])
    set_version = db.relationship('SetVersion', backref='transitions')

    def to_dict(self):
        """Convert transition to dictionary representation."""
        return {
            'id': self.id,
            'from_track_id': self.from_track_id,
            'to_track_id': self.to_track_id,
            'set_version_id': self.set_version_id,
            'transition_type': self.transition_type,
            'duration': self.duration,
            'start_position': self.start_position,
            'end_position': self.end_position,
            'parameters': self.parameters,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Transition {self.from_track_id} -> {self.to_track_id}>'
