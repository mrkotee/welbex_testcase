FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt update && apt upgrade -y && apt install -y netcat
RUN python3 -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt
#"pip install python-dotenv"

#RUN mkdir /cookbook
COPY . .
#WORKDIR /cookbook

COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
