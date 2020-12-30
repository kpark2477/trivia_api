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
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  
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

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    