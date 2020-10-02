# starwarsV
This is application to test api programming skill.

### How to build the application:

STEP_1 -> cd in starwarsV folder.
STEP_2 -> execute "docker build . -t starwars:latest --no-cache"
STEP_3 -> execute "docker run --name sarwarsV -d -p 8080:5000 starwars:latest"

### Serving 2 apis:
1) characters -> input is json example = '{"filmID":"1"}'
2) film -> input is json example = '{}'

##### local host server start:
STEP_1 -> cd into starwarsV/application
STEP_2 -> execute "python server.py"

### Commands to test on localhost:
##### Native curl on windows:
curl -X POST -H "Content-Type:application/json" --data "{"""filmID""":"""1"""}" http://localhost:5000/characters

##### On linux:
curl -X POST -H "Content-Type:application/json" --data '{"filmID":"1"}' http://localhost:5000/characters
