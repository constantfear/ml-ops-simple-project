FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /server

COPY requirements.txt /server

WORKDIR /server

RUN pip install -r requirements.txt 

COPY . /server

EXPOSE 8000

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]