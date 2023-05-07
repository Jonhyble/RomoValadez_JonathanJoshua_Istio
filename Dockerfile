FROM python:3.9

COPY ./ApiDeApis /app

RUN pip3 install -r app/requirements.txt

WORKDIR /app/src

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]