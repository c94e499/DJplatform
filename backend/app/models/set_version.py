"""SetVersion model for Mixcraft DJ Platform."""
from datetime import datetime
from app import db


class SetVersion(db.Model):
    """SetVersion model representing versions of DJ sets."""
    __tablename__ = 'set_versions'

    id = db.Column(db.Integer, primary_key=True)
    version_number = db.Column(db.Integer, nullable=False)
    commit_message = db.Column(db.String(500))
    track_order = db.Column(db.JSON)  # JSON array of track IDs in order
    set_id = db.Column(db.Integer, db.ForeignKey('sets.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert set version to dictionary representation."""
        return {
            'id': self.id,
            'version_number': self.version_number,
            'commit_message': self.commit_message,
            'track_order': self.track_order,
            'set_id': self.set_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<SetVersion {self.set_id}:v{self.version_number}>'
