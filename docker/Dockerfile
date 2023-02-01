FROM python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 69

CMD ["streamlit", "run", "app.py"]