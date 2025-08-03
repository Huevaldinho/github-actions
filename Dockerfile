FROM python:3.11-slim


# Crear un usuario y grupo sin privilegios
RUN groupadd -r appgroup && useradd -r -g appgroup appuser 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main.py .
COPY ./src ./src
COPY ./data ./data
COPY ./models ./models


# Cambiar propiedad de la carpeta /app al usuario creado
RUN chown -R appuser:appgroup /app

EXPOSE 8000

# Cambiar a usuario no root
USER appuser


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]