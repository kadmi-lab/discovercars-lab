# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app

# install the dependencies and packages in the requirements file
RUN pip install -r /app/requirements.txt

# copy every content from the local file to the image
COPY . /app


EXPOSE 3000
ENV FLASK_APP=main.py
CMD [ "flask", "run","--host","0.0.0.0","--port","3000"]