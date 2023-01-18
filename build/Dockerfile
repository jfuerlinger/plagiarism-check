FROM python:slim

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y unzip

RUN pip install -U scikit-learn scipy matplotlib wheel pandas openpyxl

WORKDIR /workspace
COPY *.py .
COPY performCheck.sh .

CMD ["./performCheck.sh"]
# CMD ["/bin/bash"]
# CMD [ "python", "./checkPlagiat.py"]
# CMD ["tail", "-f", "/dev/null"]
