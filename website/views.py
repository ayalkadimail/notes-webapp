from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method== 'POST':
        note= request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user) 


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/edit-note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("You are not allowed to edit this note.", category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        new_data = request.form.get('note')
        if len(new_data) < 1:
            flash('Note is too short!', category='error')
        else:
            note.data = new_data
            db.session.commit()
            flash('Note updated!', category='success')
            return redirect(url_for('views.home'))

    return render_template("edit_note.html", user=current_user, note=note)


@views.route('/api/notes')
@login_required
def api_notes():
    notes = [note.data for note in current_user.notes]
    return jsonify({'notes': notes})


