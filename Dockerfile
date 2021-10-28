FROM python:3.9.7-bullseye
USER root

RUN apt-get update
RUN apt-get -y upgrade
<<<<<<< HEAD
RUN apt-get -y install locales libgl1-mesa-dev git vim less libsndfile1 fluidsynth && \
=======
RUN apt-get -y install locales libgl1-mesa-dev && \
>>>>>>> b03102da7319d241884c06ebbc8f5d32c1c997f0
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /opt
ADD ./docker/opt/ /opt
RUN git clone https://github.com/huggingface/transformers

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
<<<<<<< HEAD
RUN pip install flask tweepy pretty_midi opencv-python opencv-contrib-python numpy scipy ibm-cloud-sdk-core ibm-watson goolabs midi2audio moviepy librosa matplotlib pymongo[srv] gunicorn 
=======
RUN pip install flask tweepy pretty_midi opencv-python opencv-contrib-python numpy scipy ibm-cloud-sdk-core ibm-watson goolabs midi2audio moviepy librosa matplotlib pymongo[srv]
RUN pip install gunicorn
>>>>>>> b03102da7319d241884c06ebbc8f5d32c1c997f0

RUN pip install mecab-python3 unidic-lite fugashi ipadic
CMD ["gunicorn", "app:app", "--chdir", "/opt"]
