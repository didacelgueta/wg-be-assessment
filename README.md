## Solution

#### Exercices
Run the files to check the exercices solutions. The output should be nothing as there are assertions with the final results
```
python3 exercises/exercise_1_1.py
python3 exercises/exercise_1_2.py
```

#### Application
All the necessary commands are set in the Makefile file
- Build docker with API, Postgres, Redis
```
make build
```
Once the containers are built you can browse the different endpoints in http://0.0.0.0:5000
Example: Check zipcodes with 'A' risk factor in http://0.0.0.0:5000/databases/zipcodes?risk_factor=A

By default when docker is built it will run the seeder. As postgres database has persistance, the next time you build docker you can change the RUN_SEEDER variable to False in enviroment file [.env](.env)

- Run tests
```
make test
```

- Run coverage report
```
make coverage-report
```


# WeGroup Python Examination

This project will test your general Python backend development skills.
The examination is split up in two parts:
- The first part will test your Python knowledge through some basic exerices.
- The second part focuses on testing your technical skills on an application level.

If you have any questions about the examination or something is not completely clear, please don't hesitate to contact us!

## Evaluation
Please note that the example application was designed with a lot of room for improvement for you to identify and act upon.
Feel free to make any adjustments to the example application that you deem necessary.
If you do, please make note on your decision making process so we can discuss it later on.

The evaluation of your solution will be largely based on the following categories:
- Code quality & style
    - Pythonic code
    - Performance & security
    - Refactoring
    - Linting, formatting, etc. (__tip__: pre-commit, Makefile)
- Git proficiency
    - Size and quality of commits
    - Usage of pull requests
    - Branching strategy
- Testing
    - Coverage
    - Isolation
    - Readability
    - Adding extra tests
- Quality of API
    - Route naming
    - API documentation

__Note__: Make sure your tests (unit, e2e, integration) can be run multiple times and still work (think about database writes).
If data is needed in a database make sure to write a script that does this automatically.

__Note__: Pandas/Numpy are very convenient dependencies but you should be able to complete the exercises without it.

## Part 1: Python exercises

> Provide your solutions to these exercises using their dedicated files in `exercises/`

#### EX 1.1

Write a function that takes two list of integers as input and returns the integers that are in both lists as a new list.

```
input: [1,5,70,24,155], [17,24,25,24,68,155]
$ [24,155]

input: [5,109,49,3], [63, 1, 44, 9]
$ []

input: [1,1,1,1,1], [2,2,2,2,2,2,1]
$ [1]
```

#### EX 1.2
Given a list of `Customers` instances, where a customer is defined by a `name`, an `email` and an `age`, write a function that
takes a list of customer instances as input and returns all groups of customers with the same age.

```
Given customers (name - email - age):

Joe     joe@wegroup.be      47
Sara    sara@wegroup.be     23
Alice   alice@wegroup.be    23
Bob     bob@wegroup.be      47
Gary    gary@wegroup.be     33

Expected output:
$ { 23: ["Alice", "Sara"], 47: ["Bob", "Joe"], 33: ["Gary"] }
```
##### EX 1.2.1
Provide a naive solution that does not use any extra imports. Make sure to keep performance in mind.


##### EX 1.2.2
Provide a solution that makes use of an extra import (__tip__: use an iterator from `itertools`).

## Part 2: Python application

We will be using a Python web server framework called [FastAPI](https://fastapi.tiangolo.com/) in our example application.

For exercises that require a more descriptive answer you can choose to answer them here in the README or using comments in the code itself.

### Getting started

First install [poetry](https://python-poetry.org/docs/#installation) for packaging and dependency management.
After cloning the project you can install all of the project dependencies using the following commands:

```bash
# Activate the virtual environment
poetry shell
# Install all project dependencies
poetry install
```

The project is currently configured to use `python3.9`. If you do not have this Python version installed or are more comfortable
in another version, you can reconfigure the project by:

- Changing the Python version in the `pyproject.toml` file.
- Configuring the virtual environment to use another Python version, e.g., `poetry env use python3.6`.

Verify whether you succeeded in installing the project by running the application:

```bash
# Run the application using Makefile
make run
# or run the application using poetry
poetry run uvicorn wg_be_exam.app:app --reload --workers 1 --port 5000
```

Which should look something like this:
```bash
INFO:     Will watch for changes in these directories: ['your directory']
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [16394] using statreload
INFO:     Started server process [16400]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Exercises

Everything you need to begin should already be in place. Each exercise has a file listed in which you will
be able to find a more detailed description of what is expected to complete the assignment.
A few basic tests are provided so you can verify your solution, but feel free to alter these in any way.

You can run the tests using either:

```bash
# Using the Makefile
make test
# or by using pytest inside virtualenv
pytest
# or by using poetry
poetry run pytest
```

#### EX 1: Index (NET/HTTP)

> File: [wg_be_exam/routes/index/router.py](wg_be_exam/routes/index/router.py)

Retrieve the current Belgian health index for three different base years.

#### EX 2: Zipcode (FILE IO)

> File: [wg_be_exam/routes/zipcode/router.py](wg_be_exam/routes/zipcode/router.py)

Retrieve a risk factor ("A", "B" or "C") associated with a Belgian zipcode.

#### EX 3: Database

> File: [wg_be_exam/routes/zipcode/router.py](wg_be_exam/routes/zipcode/router.py)

##### Requirements
Setup a Postgres database on your side (docker/local/server) and add the dsn to `.env` (it should be auto read and put to ENV variable).

##### EX 3.1
Make the previous exercise work without the csv file and by using a database.

##### EX 3.2
There are two issues in the example implementation of the `get_zipcode_by_risk_factor` function.
Try to identify these issues and fix the faulty implementation. Answer the subquestions to this exercise.

- __Issue 1__: Issue one involves a security issue with SQL.
- __Issue 2__: The second issue involves performance when dealing with concurrent requests. As you might have noticed, the function was not implemented in an asynchronous way.
Try to convert this function to it's async variant to resolve these possible performance issues and try confirm or study the performance improvement when dealing with concurrent requests.

### Ex 4: Caching

Implement a caching mechanism in the code (memory/redis/memcached/...) so you do not need to call the database on every request.
Where is the best place in the application to do this?

### EX 5: Docker

##### EX 5.1
Create a `Dockerfile` to build and run this application. Make use of `python:3.9-alpine` as a base and make sure to run the app in the docker as __non-root__. Keep in mind 1 docker container == 1 running process!
The container should be exposed on __port 5000__.

##### EX 5.2

Create a `docker-compose` to easily spin up the dependencies required to run the project. This should contain at least a Postgres container and might, depending on what you chose in the Caching exercise, contain a container for caching as well.
