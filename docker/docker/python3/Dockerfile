FROM python:3.9.7-bullseye
USER root

RUN apt-get update
RUN apt-get -y upgrade
<<<<<<< HEAD
RUN apt-get -y install locales libgl1-mesa-dev git && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 
=======
RUN apt-get -y install locales libgl1-mesa-dev && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
>>>>>>> 3d9ca83ce198aa389be240a83b066ef38fe5c4ec
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm



RUN apt-get install -y vim less
RUN apt-get install -y libsndfile1
RUN apt-get install -y fluidsynth
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install flask tweepy pretty_midi opencv-python opencv-contrib-python numpy scipy ibm-cloud-sdk-core ibm-watson goolabs midi2audio moviepy librosa matplotlib pymongo[srv]
<<<<<<< HEAD
RUN pip install git+https://github.com/adapter-hub/adapter-transformers.git
RUN git clone https://github.com/huggingface/transformers
RUN pip install torch
RUN pip install mecab-python3
RUN pip install unidic-lite fugashi ipadic 
=======
>>>>>>> 3d9ca83ce198aa389be240a83b066ef38fe5c4ec
