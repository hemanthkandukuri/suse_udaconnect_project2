FROM python:3.8

COPY . /persons_api_grpc
WORKDIR /persons_api_grpc
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app/main.py"]