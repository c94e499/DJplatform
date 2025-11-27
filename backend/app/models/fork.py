"""Fork model for Mixcraft DJ Platform."""
from datetime import datetime
from app import db


class Fork(db.Model):
    """Fork model representing set forking relationships."""
    __tablename__ = 'forks'

    id = db.Column(db.Integer, primary_key=True)
    original_set_id = db.Column(db.Integer, db.ForeignKey('sets.id'), nullable=False)
    forked_set_id = db.Column(db.Integer, db.ForeignKey('sets.id'), nullable=False)
    forked_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forked_at_version = db.Column(db.Integer)  # Version number at fork time
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    original_set = db.relationship('Set', foreign_keys=[original_set_id])
    forked_set = db.relationship('Set', foreign_keys=[forked_set_id])
    forked_by = db.relationship('User', backref='forks')

    def to_dict(self):
        """Convert fork to dictionary representation."""
        return {
            'id': self.id,
            'original_set_id': self.original_set_id,
            'forked_set_id': self.forked_set_id,
            'forked_by_user_id': self.forked_by_user_id,
            'forked_at_version': self.forked_at_version,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Fork {self.original_set_id} -> {self.forked_set_id}>'
