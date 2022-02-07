FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
COPY . main-fastapi.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "main-fastapi.py" ]]
ENTRYPOINT [ "python" ]