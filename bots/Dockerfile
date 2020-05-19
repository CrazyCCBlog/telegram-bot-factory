FROM python:3.5

WORKDIR /telegram

COPY ../templates/app.py .
COPY requirements-container.txt .
COPY conf.json .
RUN pip3 install -r requirements-container.txt

CMD [ "python", "./app.py" ]