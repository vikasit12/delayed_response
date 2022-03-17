FROM python:alpine3.8
COPY .. /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT [ "python" ]
CMD [ "sleep.py" ]