# Full Stack API Final Project

## Full Stack Trivia

유다시티 full stack nanodegree 코스의 프로젝트입니다.
퀴즈 문제를 풀 수 있는 웹사이트를 만드는 프로젝트이며,
유다시티에서 만들어 놓은 front-end 에 맞추어 backend 부분을 구축하는 프로젝트입니다.

front-end 파일을 살펴보고 그에 맞추어,
backend 에서 end point 별로 알맞는 data를 return할수 있도록 서버를 구축해야 합니다.
(Python flask와 postgres, sqlalchemy 활용)

서버를 설계할 능력과 프론트엔드에서 요구하는 데이터를 파악할 수 있는 능력이 요구됩니다.
CORS 및 Unittest를 통한 testing 도 포함되어 있습니다.

사이트의 주요 기능은 아래와 같습니다.

1) Display questions - 
both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
모든 question 혹은 카테고리별로 question을 display 합니다. 각각의 qeustion은 질문내용과 카테고리 그리고 난이도를 보여주고, 답안을 보여주거나 가릴수 있습니다.

2) Delete questions.
question을 지울 수 있습니다.

3) Add questions and require that they include question and answer text.
question을 추가할수 있고, 추가시 질문가 답안을 입력하게 합니다.

4) Search for questions based on a text query string.
텍스트 입력을 통해 question을 탐색할 수 있습니다.

5) Play the quiz game, randomizing either all questions or within a specific category. 
퀴즈 게임을 플레이 할 수 있습니다. 모든 question 혹은 category 별로 랜덤순서로 question을 보여줍니다.


## How to use

backend 폴더에서 flask 및 postgres 를 local 환경에서 run 하고,
frontend 폴더에서 front-end server를 run 하면 웹사이트를 이용하실 수 있습니다.
자세한 사항은 아래의 README를 읽어 주시기 바랍니다.

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)
