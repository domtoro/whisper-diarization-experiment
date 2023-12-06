#!/usr/bin/python3

import gradio as gr
import subprocess
import shutil
import tempfile
import sys

# Logger class to capture print statements
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def isatty(self):
        return False

# Redirecting stdout to Logger
sys.stdout = Logger("output.log")

def process_audio(uploaded_filepath):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = f"{temp_dir}/temp_audio.mp3"
        output_file_path = f"{temp_dir}/temp_audio.txt"

        shutil.copy(uploaded_filepath, temp_file_path)

        script_dir = "whisper-diarization"
        process_command = ["python3", "diarize_parallel.py", "--whisper-model", "large-v2", "-a", temp_file_path]

        print(f"Running command: {process_command}")

        # Use subprocess.Popen to capture real-time output
        with subprocess.Popen(process_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=script_dir) as proc:
            while True:
                line = proc.stdout.readline()
                if not line:
                    break
                print(line.strip())  # Log the line to the output.log file

        # Check if output file is created
        try:
            with open(output_file_path, "r") as file:
                result_text = file.read()
            return result_text
        except FileNotFoundError:
            return "Processing failed or output file not found."

# Function to read logs
def read_logs():
    sys.stdout.flush()
    with open("output.log", "r") as f:
        return f.read()

# Gradio interface setup
with gr.Blocks() as demo:
    with gr.Row():
        input_audio = gr.Audio(type="filepath", label="Upload Audio File")
        output_text = gr.Textbox(label="Output")
    run_button = gr.Button("Run")
    run_button.click(process_audio, input_audio, output_text)

    logs = gr.Textbox(label="Logs")
    demo.load(read_logs, None, logs, every=1)  # Update logs every second

# Launch the interface
demo.queue().launch(server_name="0.0.0.0")

