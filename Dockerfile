# syntax=docker/dockerfile:1

# Use an official NVIDIA CUDA base image
FROM nvidia/cuda:12.2.2-base-ubuntu22.04

# Metadata
LABEL maintainer="Domingo Toro (domtoro) <domingo.toro@tutanota.com>"
LABEL version="0.0.2"
LABEL source="https://github.com/domtoro/whisper-diarization-experiment"

# Set the working directory, we use /app which seems to become some pseudo-standard and we have no preference
WORKDIR /app

# Update the package list, install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies using PIP
# TODO: Check whether it might be better to use apt provided packages
# Cython, Stated in whisper-diarization readme as dependency
# gradio, Used for the webinterface
RUN pip3 install --no-cache-dir \
    cython \
    gradio

RUN git clone https://github.com/MahmoudAshraf97/whisper-diarization.git
RUN pip3 install --no-cache-dir -r whisper-diarization/requirements.txt

# Requirements for the Web-UI
RUN pip install git+https://github.com/gradio-app/gradio.git

COPY . /app/
RUN chmod +x /app/*.py


# Gradio webserver will be available on port 7860, use EXPOSE to inform container about this
# This does not automatically expose it when using docker run ..., you still need to publish it using -p 
EXPOSE 7860/tcp

# The command to run the app when the container starts
#ENTRYPOINT ["/app/run.sh"]
ENTRYPOINT ["/app/gradio-ui.py"]

