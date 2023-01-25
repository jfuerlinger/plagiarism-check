FROM python:3.11.1-slim-buster

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y unzip

RUN pip install -U scikit-learn scipy matplotlib wheel pandas openpyxl

WORKDIR /workspace
COPY *.py .
COPY entrypoint.sh .

CMD ["./entrypoint.sh"]
# CMD ["/bin/bash"]
