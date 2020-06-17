FROM python:latest

WORKDIR /app
COPY parse_metacritic.py .
COPY requirements.txt .

RUN pip install -r requirements.txt 

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD ["parse_metacritic.py"]
