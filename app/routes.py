from flask import current_app as app, request, make_response, jsonify
from . import db
from .database.models.mediafile import MediaFile
from datetime import datetime as dt

@app.route('/media/<fileid>', methods=['GET'])
def get_file(fileid):
    media_file = MediaFile.query.filter_by(id=fileid).first()
    ret = ''
    if media_file:
        ret = make_response(jsonify(media_file.serialize))
    else:
        ret = make_response(f"The file id {fileid} does not exist")
    return ret


@app.route('/media/delete/<fileid>', methods=['GET'])
def delete_file(fileid):
    media_file = MediaFile.query.filter_by(id=fileid).first()
    db.session.delete(media_file)
    db.session.commit()
    return make_response(jsonify(media_file.serialize))


@app.route('/media/add', methods=['POST'])
def create_file():
    """Create an new media file."""
    data = request.get_json()
    file_name = data['file_name']
    media_type = data['media_type']
    if file_name and media_type:
        new_media = MediaFile(file_name=file_name,
                              media_type=media_type,
                              created_dt=dt.now(),
                              updated_dt=dt.now())
        db.session.add(new_media)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_media} successfully created!")
    else:
        return make_response(f"File name or type can't be null!")


@app.route('/media/update', methods=['POST'])
def update_file():
    """Create an new media file."""
    data = request.get_json()
    fileid = data['id']
    file_name = data['file_name']
    media_type = data['media_type']
    response = ''
    media_file = MediaFile.query.filter_by(id=fileid).first()
    if media_file:
        if file_name:
            media_file.file_name = file_name
        if media_type:
            media_file.media_type = media_type
        media_file.updated_dt = dt.now()
        db.session.commit()
        response = f'ID {fileid} Updated Successfully'
    else:
        response = f'ID {fileid} not found'
    return make_response(response)
