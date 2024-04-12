# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

ADD main.py .

RUN pip install numpy python-dotenv

WORKDIR /app

COPY board.py game.py player.py . /app/

CMD ["python", "/app/main.py"]
