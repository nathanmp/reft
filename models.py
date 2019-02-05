from datetime import datetime
from flask import Flask, request, render_template
from flask_login import LoginManager, current_user, login_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import connexion
import sqlite3
import json
import sys
import os
from eatr import db
from werkzeug.security import generate_password_hash, check_password_hash

class FoodType(db.Model):
	__tablename__ = "foodtype"
	ftid = db.Column(db.Integer, primary_key=True)
	food_name = db.Column(db.String(64))
	serv_name = db.Column(db.String(64))
	protein_amt = db.Column(db.Integer())
	carb_amt = db.Column(db.Integer())
	fat_amt = db.Column(db.Integer())
	def __repr__(self):
		return ("<FoodType Number {}, Name {}, SS {}>").format(self.id, self.food_name, self.serv_name)

""" @login.user_loader
def load_user(id):
	return User.query.get(int(id)) """

class User(UserMixin, db.Model):
	__tablename__ = "user"
	uid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True)
	email = db.Column(db.String(128), unique=True)
	password_hash = db.Column(db.String(128), unique=True)
	food_types = db.Column(db.String(400))
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class FoodElement(db.Model):
	def __init__(self, food_id, serving, username="Guest"):
		self.fid = food_id
		self.sid = serving	
		self.uid = username
		self.timestamp = datetime.utcnow()
	def __repr__(self):
		return ("<FoodElement, EID {}, FID {}, Username {}, SS {}>").format(self.eid, self.fid, self.uid, self.sid)
	eid = db.Column(db.Integer, primary_key=True)
	fid = db.Column(db.Integer, db.ForeignKey('foodtype.ftid'))
	sid = db.Column(db.Float)
	uid = db.Column(db.String(64), db.ForeignKey('user.uid'))
	timestamp = db.Column(db.Integer, default=datetime.utcnow)