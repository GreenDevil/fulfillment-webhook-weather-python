FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests

COPY . .

ENV PORT=5000
EXPOSE 5000
CMD [ "python", "./app.py" ]
