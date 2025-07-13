FROM python:3.11-alpine

WORKDIR /app 
RUN pip install flask
COPY . .

EXPOSE 5005

CMD ["flask","run","--host","0.0.0.0"]