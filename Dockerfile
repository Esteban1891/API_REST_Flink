# This dockerfile allows you 
# to install python the package requirements
# lift the django / python application with gunicorn

FROM python:3.9.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "backend", "backend.wsgi:application"]