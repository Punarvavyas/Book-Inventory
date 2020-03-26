FROM python:3.6.5-alpine
WORKDIR /code
ENV FLASK_APP flasknotes.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN pip install flask_cors==3.0.8
CMD ["python", "flasknotes.py"]
