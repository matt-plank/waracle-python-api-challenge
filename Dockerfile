FROM python:3.10

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY cake_api cake_api
COPY pyproject.toml /pyproject.toml
RUN pip install .

EXPOSE 8000

CMD ["uvicorn", "cake_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
