FROM python:3.9-slim-buster AS base

FROM base AS builder

WORKDIR /app
COPY . .

RUN pip install "poetry>=1.0.0"
RUN poetry config virtualenvs.create false
RUN poetry install

# TODO: Add runtime stage that copies env to runtime and gets rid of poetry 300MB --> 100MB
# FROM base AS runtime
# COPY --from=builder /usr/local/bin/ /usr/local/bin/
# docker run --publish 8000:5000 python-docke
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]