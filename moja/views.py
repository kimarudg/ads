"""
Copyright (c) 2016, BRCK Inc
All Rights Reserved
"""
import time
from datetime import datetime
import os
from flask import Blueprint, jsonify, render_template, request, session, redirect
from moja import db
from datetime import datetime, timedelta
from moja.models import Placements, Brck, Campaigns
from sqlalchemy import and_

moja = Blueprint('moja', __name__,
                  template_folder='templates')


@moja.route('/')
@moja.route('/gatead')
def gatead():
    """Displays the gate add"""
    brck = Brck.query.first()
    campaign = Campaigns.query.first()
    previous = request.args.get('previous')
    if previous != "":
        records  = Placements.query.filter(and_(Placements.id != previous, Placements.ad_unit == 'gate'))
    else:
        records  = Placements.query.filter(Placements.ad_unit == 'gate')
    return jsonify({'ads':[record.to_json() for record in records], 'bundle':brck.bundle_id, 'campaign':campaign.id})

@moja.route('/masthead', methods=['GET'])
def ads():
    records  = Placements.query.filter(Placements.ad_unit != 'gate')
    brck = Brck.query.first()
    campaign = Campaigns.query.first()
    return jsonify({'ads':[record.to_json() for record in records], 'bundle':brck.bundle_id, 'campaign':campaign.id})
