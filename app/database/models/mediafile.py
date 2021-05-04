from app import db


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class MediaFile(db.Model):
    """Model for accounts."""

    __tablename__ = 'media_file'

    id = db.Column(db.Integer,
                   primary_key=True)
    file_name = db.Column(db.String(250),
                          index=False,
                          unique=True,
                          nullable=False)
    media_type = db.Column(db.String(50),
                           index=False,
                           unique=True,
                           nullable=False)
    created_dt = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=False)
    updated_dt = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'media_type': self.media_type,
            'created_dt': dump_datetime(self.created_dt),
            'updated_dt': dump_datetime(self.updated_dt)
        }

    def __repr__(self):
        return '<MediaFile {}>'.format(self.id)
