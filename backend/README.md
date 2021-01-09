### Installing Dependencies

#### Python 3.7

python 3.7 이상의 버전이 필요합니다.
[python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment 가상환경설정

python dependency를 install 하기 전에 가급적
virtual environment를 활용하시길 바랍니다.
[python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies 

virtual environment setup하고 running 하셨다면, `/backend` 폴더로 들어가셔서 아래의 명령어를 입력해 주세요:

```bash
pip install -r requirements.txt
```

`requirements.txt` 안에 있는 dependency들이 install 됩니다.

##### Key Dependencies (주요 dependency)

- [Flask](http://flask.pocoo.org/)  은 python의 backend microservices framework입니다. requests 와 responses를 처리하기 위해 이용됩니다.

- [SQLAlchemy](https://www.sqlalchemy.org/) 은 Python SQL toolkit 이자 ORM 입니다. postgres database를 다룹니다.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) flask의 extention으로 frontend server로 부터의 request를 처리하는데 사용됩니다.

## Database Setup

PC에 postgres를 설치하시고 'trivia'라는 이름으로 database를 생성해주세요.
Postgres가 실행되고 있을때 backend 폴더에 있는 trivia.psql 파일을 통해서
테이블과 데이터들을 trivia db에 생성해 주세요.

backend folder에서 terminal을 열고:
```bash
psql trivia < trivia.psql
```

backend 폴더의 models.py 7번 라인에 database path를 설정해주십시오.
default 값은 아래와 같습니다.
'postgresql://postgres:1111@localhost:5432/trivia'

-> 'postgresql://YourPostgresID:Password@localhost:5432/trivia'

## Running the server

DB setup과 가상환경설정을 통한 dependency install을 마치셨다면,
가상환경에 들어가시고 서버를 run 하시기 바랍니다.

backend 폴더에서 아래의 명령어를 terminal에 입력하세요:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

`FLASK_ENV` variable 을 `development` 로 세팅하면 file change를 detect하고 서버를 자동적으로 restart합니다.
`FLASK_APP` variable 을 `flaskr` 로 세팅하면 flask 가 `flaskr` 디렉토리를 찾아  `__init__.py` 을 실행하도록 합니다.


## Testing

unittest를 통해서 endpoint들을 test해보실수 있습니다.
trivia_test라는 별도의 db를 생성하시고, test_flask.py 파일에 19번째 line에서 db path 설정을 해주시기 바랍니다.
path 설정방식은 상기의 Database Setup 항목과 같습니다.

그 후에 test를 실행하시려면

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```



## End points 별 설명 및 sample response입니다.

GET '/categories'
General : 
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category

Sample :
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}



GET '/questions'
General : 
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Fetches a dictionary of questions in which the keys are answer, category, difficulty, id, question and the values are the corresponding string of the keys

- Sample : 
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 23
}




DELETE '/questions/<int:question_id>'
General : 
- Delete question using a question ID on the endpoint
- This removal will persist in the database and when you refresh the page

- Sample : 
{
  "deleted": 5,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ],
  "success": true,
  "totalQuestions": 22
}





POST '/questions'
General : 
- POST a new question which will require the question and answer text, category, and difficulty score.
- This will add new row in the database and when you refresh the page it will show the id of the created question

- Sample : 
{
  "created": 40,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ],
  "success": true,
  "total questions": 24
}



POST '/questions/search'
General : 
- Get questions based on a search term
- It should return any questions for which the search term is a substring of the question

- Sample :
- The questions list will update to include only question that include that string within their question
- For this sample I used the search term "title"
{
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "totalQuestions": 24
}




GET '/categories/<int:category_id>/questions'
General : 
- Get questions based on on category
- It should return any questions of which category is on the endpoint

- Sample :
{
  "currentCategory": {
    "id": 1,
    "type": "Science"
  },
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "dddddd",
      "category": 1,
      "difficulty": 1,
      "id": 36,
      "question": "ffffff"
    },
    {
      "answer": "aa",
      "category": 1,
      "difficulty": 1,
      "id": 37,
      "question": "fffffffff"
    }
  ],
  "success": true,
  "totalQuestions": 17
}




POST '/quizzes'
General : 
- Get questions to play the quiz
- This endpoint takes category and previous question parameters and return a random questions within the given category, 
if provided, and that is not one of the previous questions

- Sample :
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  }
}