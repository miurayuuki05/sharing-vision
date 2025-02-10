from flask import Flask, jsonify, request
from flask import Blueprint
from app.database import db
from datetime import datetime
from app.model import Article

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Welcome to the home page")

@main.route('/article', methods=['POST'])
def post_article():
    request_data = request.get_json()

    article = Article(
        title=request_data['title'],
        content=request_data['content'],
        category=request_data['category'],
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status=request_data['status']
    )

    db.session.add(article)
    db.session.commit()

    return jsonify(article.to_dict())

@main.route('/article/<int:limit>/<int:offset>', methods=['GET'])
def get_articles(limit, offset):
    articles = db.session.query(Article).limit(limit).offset(offset)
    return jsonify([article.serialize() for article in articles])

@main.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    article = db.session.query(Article).get(id)
    return jsonify(article.serialize())

@main.route('/article/<int:id>', methods=['PUT'])
def put_article(id):
    article = Article.query.get(id)
    request_data = request.get_json()

    article.title = request_data['title'] if 'title' in request_data else article.title
    article.content = request_data['content'] if 'content' in request_data else article.content
    article.category = request_data['category'] if 'category' in request_data else article.category
    article.updated_at = datetime.now() 
    article.status = request_data['status'] if 'status' in request_data else article.status

    db.session.commit()

    return jsonify(article.serialize())

@main.route('/article/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return jsonify(article.serialize())