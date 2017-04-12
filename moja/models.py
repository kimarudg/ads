"""
BRCK moja
@module: models
@description: Utility for SQLAlchemy

Copyright (C) 2016
BRCK Inc, all rights reserved
"""

from sqlalchemy import Boolean, Column, ForeignKey, Index, Integer, LargeBinary, String, Table, Text, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
# from moja import db
from moja import db


Base = declarative_base()
metadata = Base.metadata

t_packages_tags = db.Table(
    'packages_tags',
    db.Column('package_id', String(128), db.ForeignKey("packages.id")),
    db.Column('tag_id', String(128), db.ForeignKey("tags.id")),
)

t_channels_packages = db.Table(
    'channels_packages',
    db.Column('package_id', String(128), db.ForeignKey("packages.id")),
    db.Column('channel_id', String(128), db.ForeignKey("channels.id")),
)

class Asset(db.Model):
    """
        Model Description for Assets
    """
    __tablename__ = u'assets'

    id = Column(String(128), primary_key=True)
    package_id = Column(String(128), ForeignKey('packages.id'))
    title = Column(String(128))
    description = Column(String(128))
    src = Column(String(128))
    content_type = Column(String(128))
    is_default = Column(Boolean, nullable=False, server_default=text("0"))
    package = db.relationship("Package", back_populates='assets')


class Bundle(db.Model):
    """
        Model Description for Bundles
    """
    __tablename__ = u'bundle'

    id = Column(String(128), primary_key=True)
    name = Column(String(128), nullable=False)
    size = Column(Integer)
    bundle_version = Column(Integer, nullable=False, server_default=text("0"))


class Category(db.Model):
    """
        Model Description for Category
    """
    __tablename__ = u'categories'

    id = Column(String(128), primary_key=True)
    name = Column(String(128), nullable=False)
    label = Column(String(128), nullable=False)



class Package(db.Model):
    """
        Model Description for Package
    """
    __tablename__ = 'packages'

    id = Column(String(128), primary_key=True)
    category_id = Column(String(128), index=True)
    title = Column(String(128), nullable=False)
    description = Column(Text(128))
    type = Column(Text(128))
    torrent_hash = Column(String(128), nullable=False)
    size = Column(Integer)
    has_poster = Column(Boolean, nullable=False, server_default=text("0"))
    has_thumbnail = Column(Boolean, nullable=False, server_default=text("0"))
    # featured = Column(Boolean, nullable=False, server_default=text("0"))
    created = Column(Integer, nullable=False, server_default=text("0"))
    updated = Column(Integer, nullable=False, server_default=text("0"))
    tags = db.relationship("Tag", secondary=t_packages_tags, backref=db.backref('tags',lazy='dynamic'))
    assets = db.relationship("Asset", back_populates='package')
    channel = db.relationship("Channels", secondary=t_channels_packages, backref=db.backref('channels',lazy='dynamic'))


class Tag(db.Model):
    """
        Model Description for Tags
    """
    __tablename__ = u'tags'

    id = Column(String(128), primary_key=True)
    category_id = Column(String(128))
    tag_group_id = Column(String(128), index=True)
    name = Column(String(128), nullable=False)
    packages = relationship("Package", secondary=t_packages_tags, backref=db.backref('packages', lazy='dynamic'))


class TagGroup(db.Model):
    """
        Model Description for TagGroup
    """
    __tablename__ = u'tag_groups'

    id = Column(String(128), primary_key=True)
    name = Column(String(128), nullable=False)
    label = Column(String(128), nullable=False)


class Placements(db.Model):
    """
        Model Description for Placements
    """
    __tablename__ = u'placements'

    id = Column(String(128), primary_key=True)
    campaign_id = Column(String(128), index=True)
    creative_id = Column(String(128), index=True)
    ad_unit = Column(String(128), nullable=False)
    src = Column(String(128), nullable=False)
    content_type = Column(String(128), nullable=False)
    # Return the ad as JSON
    def to_json(self):
        ad = {
            'id' : self.id,
            'campaign_id' : self.campaign_id,
            'creative_id': self.creative_id,
            'ad_unit' : self.ad_unit,
            'src':self.src,
            'content_type':self.content_type,
        }
        return ad


class Campaigns(db.Model):
    """
        Model Description for Campaigns
    """
    __tablename__ = u'campaigns'

    id = Column(String(128), primary_key=True)
    name = Column(String(128), nullable=False)
    weight = Column(Integer)
    impressions = Column(Integer)


class Brck(db.Model):
    """
        Model Description for BRCK
    """
    __tablename__ = u'brck'

    bundle_id = Column(String(128), primary_key=True)
    bundle_version = Column(Integer)
    name = Column(String(128), nullable=False)
    size = Column(Integer)
    token = Column(Text(128))
    longitude = Column(String(128))
    latitude = Column(String(128))

class Interactions(db.Model):
    """
        Model Description for Interactions
    """
    __tablename__ = u'interactions'

    item_id = Column(String(128), primary_key=True)
    item_type = Column(String(30))
    timestamp = Column(Integer)
    action = Column(String(30))

class Channels(db.Model):
    """
        Model description for Channels.
    """
    __tablename__ = u'channels'
    id = Column(String(128), primary_key=True)
    name = Column(String(128))
    label = Column(String(128))
    has_logo = Column(Boolean, nullable=False, server_default=text("0"))
    package_channel = relationship("Package", secondary=t_channels_packages, backref=db.backref('channels', lazy='dynamic'))
