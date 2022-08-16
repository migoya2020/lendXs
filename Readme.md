***LendXs Developer Home Test:***

**How to run this code:**

-- Note: this project uses python 3.9^
1. install poetry if you dont have it: https://python-poetry.org/docs/#installing-with-pip
2. Navigate inside the  lendxs directory
3. Run ```poetry install```
4. Activate environment run ```poetry shell```
5. rename ```.env_example```  to ```.env```
6. Make sure  RabbitMQ is tunning, or you can fire up the docker version  by running ```docker-compose up```

7. one one terminal  ```run python consumer_lendxs.py```

8. open  a second terminal and  run ```python send_lendxs.py```

you should see the  received messages logged on the terminal

**By: David Migoya** 
```dmigoya@gmail.com```
