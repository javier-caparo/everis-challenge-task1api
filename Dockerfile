FROM python:3.8.6-alpine

ENV PROJECT_DIR /usr/src/task1api
ENV HOSTNAME sandbox

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pip install pipenv
RUN pipenv install --skip-lock

EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]