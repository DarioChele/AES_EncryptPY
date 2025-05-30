FROM python:3.10-slim
WORKDIR /app
COPY EncryptDecrypt_AES.py .
COPY dict.json .
RUN pip install cryptography
ENTRYPOINT ["python", "EncryptDecrypt_AES.py"]