FROM python:3.9-slim-bullseye AS builder

WORKDIR /app
COPY . .

RUN apt update -y && apt upgrade -y && apt install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN $HOME/.poetry/bin/poetry config virtualenvs.create false 
RUN $HOME/.poetry/bin/poetry install --no-dev 
RUN $HOME/.poetry/bin/poetry export -f requirements.txt >> requirements.txt

FROM python:3.9-slim-bullseye AS runtime

RUN mkdir /app
COPY src /app
COPY --from=builder /app/requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# docker run --publish 8000:5000 python-docke
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]