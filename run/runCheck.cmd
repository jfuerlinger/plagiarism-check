docker pull jfuerlinger/duplicate:latest
docker run -it --rm -v %cd%:/input --name DuplicateCheck jfuerlinger/duplicate:latest
