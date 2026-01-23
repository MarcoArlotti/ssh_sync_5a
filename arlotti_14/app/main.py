# app/main.py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.repository.canali_repositories import get_channel
from app.repository.video_repositories import get_videos

bp = Blueprint('main', __name__)

@bp.route('/channel')
def index():
    channels_py = get_channel()
    return render_template("stampa_canali.html", channels_html=channels_py)

@bp.route('/channel/<int:canale_id>')
def channel(canale_id):
    video_py = get_videos(canale_id)
    return render_template("channel.html",videos_html=video_py)
