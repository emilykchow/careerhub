FROM python:3.11

# set the working directory inside the container
WORKDIR /app

RUN python -m venv .venv

ENV PATH="/app/.venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ /app/app/

EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
# RUN useradd app
# USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]