from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .models import Note
import json


views = Blueprint('views', __name__)

@views.route("/", methods=['POST', 'GET'])
@login_required
def home():

    if request.method == 'POST':
        note_text = request.form.get('note')

        new_note = Note(data=note_text, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST', 'GET'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})