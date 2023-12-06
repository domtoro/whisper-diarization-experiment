# Whisper Diarization Experiment

## Overview

This repository contains a Dockerized application for audio diarization using the Whisper model. It leverages NVIDIA CUDA for performance optimization and includes a Gradio-based web interface for easy interaction.

## Features

- **NVIDIA CUDA Base**: Utilizes NVIDIA CUDA for efficient processing.
- **Gradio Web Interface**: Provides a user-friendly interface for audio file processing.
- **Audio Diarization**: Implements diarization using the Whisper model for audio files.

## Prerequisites

- Docker
- NVIDIA GPU with CUDA support

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/domtoro/whisper-diarization-experiment.git
   cd whisper-diarization-experiment
   ```
2. **Build the Docker Image**:
   ```bash
   docker build -t domtoro/whisper-diarization-experiment:0.0.1 .
   ```

## Usage
1. **Access the Gradio Interface**:
   Open a web browser and navigate to http://localhost:7860 to use the Gradio interface.
2. **Upload Audio File**:
   Use the Gradio interface to upload an audio file for diarization.
3. **View Results**:
   After processing, the diarization results will be displayed on the Gradio interface.
