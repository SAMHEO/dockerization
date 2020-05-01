FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=5s --timeout=3s \
    CMD curl --fail http://localhost:5000/blabs || exit 1