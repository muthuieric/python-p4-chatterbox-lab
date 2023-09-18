from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET'])
def messages():
    messages = Message.query.order_by(Message.created_at).all()

    messages_serialized = [message.to_dict() for message in messages]

    response = make_response(
        messages_serialized,
        200
    )
    return response

@app.route('/messages', methods=['POST'])
def create_message():
    new_message = Message(
        body=request.json.get('body'),  
        username=request.json.get('username'),
    )

    db.session.add(new_message)
    db.session.commit()

    new_message_serialized = new_message.to_dict()

    response = make_response(
        jsonify(new_message_serialized),
        201
    )
    return response

@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = db.session.get(Message, id)  

    if message is None:
        response_body = {
            "message": "Message not found."
        }
        return jsonify(response_body), 404

    # Update the message body
    new_body = request.json.get("body")
    if new_body:
        message.body = new_body

    db.session.commit()

    updated_message_serialized = message.to_dict()

    response = make_response(
        jsonify(updated_message_serialized),
        200
    )

    return response



@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.filter_by(id=id).first()

    db.session.delete(message)
    db.session.commit()

    response_body = {
        "delete_successful": True,
        "message": "Message deleted."    
        }
    
    response = make_response(
        jsonify(response_body),
        200
    )

    return response


if __name__ == '__main__':
    app.run(port=5555)
