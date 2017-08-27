FROM python:3-slim
EXPOSE 5000
ADD app.py .
CMD ["python", "-u", "app.py"]
