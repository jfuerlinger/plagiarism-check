docker build -t duplicate:latest .

docker tag duplicate:latest jfuerlinger/duplicate:latest .
docker push jfuerlinger/duplicate:latest

