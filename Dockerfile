FROM python:3.10.12

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD hello.py ./

CMD ["python", "hello.py"]