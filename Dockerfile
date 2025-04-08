FROM ubuntu

RUN apt update -y
RUN apt install python3 python3-pip pipenv -y

WORKDIR /app
COPY . .
RUN pipenv install -r requirements.txt

EXPOSE 8080

CMD ["pipenv", "run", "python3", "main.py"]
