FROM python:3 AS base
WORKDIR /app
RUN pip install flask requests
COPY *.py .

# Stage for testing
FROM base AS test
COPY testing .
RUN pip install pytest requests-mock
CMD ["pytest", "-v", "functional_test.py"]

# Stage for running
FROM base AS run
EXPOSE 8080
CMD ["python", "app.py"]