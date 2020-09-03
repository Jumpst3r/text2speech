FROM python:3.7

WORKDIR /input

COPY . /input/

RUN pip install --upgrade pip && \
    pip install googletrans pydub gtts && \
    mkdir /output
RUN chmod +x script.sh
CMD /bin/bash
RUN apt update && apt install -yq ffmpeg
