import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
        )
      response.headers.add(
        'Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS'
        )

      return response
  
  @app.route('/categories')
  def retrieve_categories():
      selected_categories = Category.query.order_by(Category.id).all()
      formatted_categories = {}
      for category in selected_categories:
        dict_adding = {str(category.id): str(category.type)}
        formatted_categories.update(dict_adding)

      return jsonify({
        'success' : True,
        'categories' : formatted_categories
      })

  @app.route('/questions')
  def retrieve_questions():
      selected_questions = Question.query.order_by(Question.id).all()
      paged_questions = paginate_questions(request, selected_questions)

      selected_categories = Category.query.order_by(Category.id).all()
      formatted_categories = {}
      for category in selected_categories:
          dict_adding = {str(category.id): str(category.type)}
          formatted_categories.update(dict_adding)

      return jsonify({
        'success': True,
        'questions' : paged_questions,
        'total_questions': len(Question.query.all()),
        'categories': formatted_categories,
        'current_category': None
      })
  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
      question = Question.query.filter(Question.id == question_id).one_or_none()
      if question is None:
          abort(404)

      try:
          question.delete()
          selection = Question.query.order_by(Question.id).all()
          paged_questions = paginate_questions(request, selection)

          return jsonify({
            'success': True,
            'deleted': question_id,
            'questions': paged_questions,
            'totalQuestions': len(Question.query.all())
          })

      except:
          abort(422)

  @app.route('/questions', methods=['POST'])
  def create_question():
      body = request.get_json()

      new_question = body.get('question', None)
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty = body.get('difficulty', None)

      try:
          question = Question(
            question=new_question,
            answer=new_answer,
            category=new_category,
            difficulty=new_difficulty
            )

          question.insert()

          selection = Question.query.order_by(Question.id).all()
          paged_questions = paginate_questions(request, selection)

          return jsonify({
            'success': True,
            'created': question.id,
            'questions': paged_questions,
            'total questions': len(Question.query.all())
          })

      except:
          abort(422)

  @app.route('/questions/search', methods=['POST'])
  def search_question():
      body = request.get_json()
      search = body.get('searchTerm', None)

      try:
          selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
          paged_questions = paginate_questions(request, selection)

          return jsonify({
            'success': True,
            'questions': paged_questions,
            'totalQuestions': len(Question.query.all())
          })

      except:
          abort(422)

  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def retrieve_questions_by_category(category_id):
      selected_questions = Question.query.order_by(Question.id).filter(Question.category == category_id)
      paged_questions = paginate_questions(request, selected_questions)

      selected_category = Category.query.filter(Category.id == category_id).one_or_none()
      formatted_categories = selected_category.format()

      return jsonify({
        'success': True,
        'questions': paged_questions,
        'totalQuestions': len(Question.query.all()),
        'currentCategory': formatted_categories
      })

  @app.route('/quizzes', methods=['POST'])
  def retrieve_questions_for_quiz():
      body = request.get_json()
      previous_questions = body.get('previous_questions', None)
      quiz_category = body.get('quiz_category', None)

      quiz_category_id = quiz_category.get('id')

      if quiz_category_id == 0:
          questions = Question.query.filter(~Question.id.in_(previous_questions)).all()
      else:
          questions = Question.query.filter(
            Question.category == quiz_category_id).filter(~Question.id.in_(previous_questions)).all()

      if len(questions) == 0:
          return jsonify({
            'question': None
          })

      try:
          formatted_questions = [question.format() for question in questions]
          random_number = random.randrange(0, len(formatted_questions))
          random_question = formatted_questions[random_number]

          return jsonify({
            'question': random_question
          })

      except:
          abort(422)
  
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "Not found"
          }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Unprocessable"
          }), 422

  return app

    