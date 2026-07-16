# YouTube Video Downloader

A desktop-based Python application that downloads YouTube videos in the highest available quality and automatically merges audio and video streams using FFmpeg.

## Features

* Download YouTube videos in high resolution
* Automatic audio/video merging
* GUI folder selection using Tkinter
* Filename sanitization
* FFmpeg integration
* Fallback re-encoding support
* Automatic cleanup of temporary files

## Technologies Used

* Python 3
* PyTubeFix
* FFmpeg
* Tkinter
* Subprocess
* Regular Expressions

## Installation

Install the required packages:

```bash
pip install pytubefix
```

Install FFmpeg:

### Ubuntu

```bash
sudo apt install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Windows

Download FFmpeg and add it to your system PATH.

## How to Run

```bash
python YoutubeVideoDownloader.py
```

1. Enter a YouTube URL.
2. Select a download folder.
3. Wait for the video to download and merge.
4. Enjoy your downloaded video.

## Project Structure

```text
Youtube-Video-Downloader/
├── YoutubeVideoDownloader.py
└── README.md
```

## Technical Highlights

* Uses adaptive streams for maximum quality.
* Merges audio and video using FFmpeg.
* Falls back to re-encoding when direct muxing fails.
* Automatically removes temporary files after completion.


This project is intended for educational purposes only. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws.
