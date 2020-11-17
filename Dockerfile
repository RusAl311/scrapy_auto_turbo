FROM python:3.8-slim

LABEL Name="scrapy-auto-turbo"
#Directory for app
WORKDIR /scrapy-auto-turbo

#install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libpq-dev \
                        gcc
RUN pip install -r requirements.txt

COPY /auto .

# CMD ["python", "scrapy crawl autos -o data.json"]



