from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config ['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "item.db"

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(100))

@api.route('/allItems')
class AllItems(Resource):
    def get(self):
        return {'item': str(items)}

items = {}

@api.route('/<string:item_id>')
class ToDoSimple(Resource):
    def get(self, item_id):
        return {item_id: items[item_id]}
    
    def put(self, item_id):
        items[item_id] = request.form['data']
        return {item_id: items[item_id]}