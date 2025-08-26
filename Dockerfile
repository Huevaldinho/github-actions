FROM python:3.9.23-trixie

RUN groupadd -r appgroup && useradd -r -g appgroup appuser 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main.py .
COPY ./src ./src
COPY ./data ./data

RUN chown -R appuser:appgroup /app

EXPOSE 8000

USER appuser

ENTRYPOINT [ "python", "main.py" ]