from pytubefix import YouTube
import subprocess
import os
import re
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    yt = YouTube(url)

    video_stream = yt.streams.filter(adaptive=True, only_video=True) \
                            .order_by("resolution").desc().first()
    audio_stream = yt.streams.filter(adaptive=True, only_audio=True) \
                            .order_by("abr").desc().first()

    if video_stream is None or audio_stream is None:
        raise RuntimeError("Could not find a suitable video/audio stream.")

    video_path = video_stream.download(output_path=".", filename="video_temp.mp4")
    audio_path = audio_stream.download(output_path=".", filename="audio_temp.mp4")

    safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title)
    output_path = os.path.join(".", f"{safe_title}.mp4")

    result = subprocess.run([
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "copy",
        output_path
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Copy mux failed, re-encoding instead...")
        print(result.stderr)
        result = subprocess.run([
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            output_path
        ], capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stderr)
            raise RuntimeError("ffmpeg failed on both copy and re-encode.")

    os.remove(video_path)
    os.remove(audio_path)
    print(f"Downloaded {video_stream.resolution} successfully!")


def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder {folder}")
    return folder



if __name__=="__main__":
    root=tk.Tk()
    root.withdraw()
    video_url=input("Please enter a youtube url ")
    save_dir=open_file_dialog()
    if not save_dir:
        print("no such folder")
    else:
        download_video(video_url,save_dir)
