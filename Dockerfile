FROM python:3.9.7-bullseye
USER root

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install locales libgl1-mesa-dev && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /opt
ADD ./docker/opt/ /opt

RUN apt-get install -y vim less
RUN apt-get install -y libsndfile1
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install flask tweepy pretty_midi opencv-python opencv-contrib-python numpy scipy ibm-cloud-sdk-core ibm-watson goolabs midi2audio moviepy librosa matplotlib pymongo[srv]
RUN pip install gunicorn

CMD ["gunicorn", "docker/opt/app:app(1)", "--chdir", "docker/opt/"]
