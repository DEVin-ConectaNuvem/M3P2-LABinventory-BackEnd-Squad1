FROM python:3.10-alpine

ENV HOST=0.0.0.0
ENV PORT=5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]
