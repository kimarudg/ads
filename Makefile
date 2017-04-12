#
# Copyright (c) 2016. BRCK LTD.
#
# This software is licensed under the BRCK License v1.
# See LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=moja-ads
PKG_VERSION:=v1.0.0-alpha.2

PKG_RELEASE:=$(PKG_SOURCE_VERSION)
PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=git@github.com:brck/moja-ads.git
PKG_SOURCE_VERSION:=$(PKG_VERSION)
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION)-$(PKG_SOURCE_VERSION).tar.gz

PKG_BUILD_PARALLEL:=1

include $(INCLUDE_DIR)/package.mk

# an empty Build/Compile section ensures that the "make"
# phase of package creation does not fail
define Build/Compile
endef

define Package/moja-ads
	SECTION:=moja-ads
	CATEGORY:=BRCK
	TITLE:=BRCK Moja Ads Service
	URL:=http://www.brck.com
	DEPENDS:=+supabrck-core \
	         +python \
			 +python-eventlet \
			 +python-psutil \
			 +python-gevent \
			 +python-gunicorn \
			 +python-flask \
			 +python-flask-socketio \
			 +python-alembic \
             +nginx \
endef

define Package/moja-ads/description
	A content and connectivity platform
	It leverages the connectivity of SupaBRCK to provide users with a convenient,
	fast and easy way to consume relevant, meaningful content on their devices
endef


define Package/moja-ads/install
	$(INSTALL_DIR) $(1)/
	$(INSTALL_DIR) $(1)/usr/share/moja-ads

	mkdir -p $(1)/externaldrive/bundle

	$(CP) $(PKG_BUILD_DIR)/moja-ads $(1)/usr/share/moja-ads
	$(CP) $(PKG_BUILD_DIR)/app.py $(1)/usr/share/moja-ads
	$(CP) $(PKG_BUILD_DIR)/requirements.txt $(1)/usr/share/moja-ads
	$(CP) $(PKG_BUILD_DIR)/conf/* $(1)/
endef

define Package/moja-ads/postinst
	#!/bin/sh

	# Install python packages
	logger -t Moja-Ads "Installing Python packages"
	pip install -r /usr/share/moja-ads/requirements.txt
	logger -t Moja-Ads "Installation of Python packages is complete"

	# Set up Flask Server
	logger -t Moja-Ads "Set up Flask server script"
	chmod a+x /etc/init.d/moja-ads

	logger -t Moja-Ads "Done setting up server script"

	# Add ads.brck.net
	echo "ads.brck.net  192.168.88.1" >> /etc/hosts

	# Restart NGINX for Moja configs to take place
	logger -t Moja-Ads "Restart NGINX"
	/etc/init.d/nginx restart

	logger -t Moja-Ads "Moja-Ads NGINX configuration is now in place"

	logger -t Moja-Ads "********* MOJA ADS SERVICE IS COMPLETE! *********"

	exit 0

endef

$(eval $(call BuildPackage,moja-ads))
