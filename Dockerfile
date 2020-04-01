FROM python:3.7

MAINTAINER shamsad alam "alam.shams.1996@gmail.com"

WORKDIR /app
COPY source_code/ /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["run.py"]