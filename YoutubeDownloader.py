from pytube import YouTube
import re
import os

def get_video_id(link):
    # Try to extract video ID using regex for various YouTube link formats
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",  # Standard video link
        r"youtu.be\/([0-9A-Za-z_-]{11})",  # Shortened video link
    ]

    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1)

    return None

def print_streams_info(streams):
    resolutions = [stream.resolution for stream in streams]
    for i, resolution in enumerate(resolutions):
        print(f"{i + 1}. {resolution}")

def on_progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rDownloading... {percentage:.2f}% complete", end="", flush=True)

def Downloader(link, save_path="."):
    try:
        video_id = get_video_id(link)

        if not video_id:
            print("Invalid YouTube link.")
            return

        youtube_object = YouTube(link, on_progress_callback=on_progress_callback)
        streams = youtube_object.streams.filter(file_extension="mp4", progressive=True).order_by("resolution")

        if not streams:
            print("No video streams found.")
            return

        # Create a new folder named "Pydownloader"
        download_folder = os.path.join(save_path, "Pydownloader")
        os.makedirs(download_folder, exist_ok=True)

        print("Available video resolutions:")
        print_streams_info(streams)

        choice = int(input("Enter the number corresponding to the desired resolution: "))
        selected_stream = streams[choice - 1]

        # Save the video inside the "Pydownloader" folder
        download_path = os.path.join(download_folder, f"{video_id}_{selected_stream.resolution}.mp4")
        selected_stream.download(download_path)

        print(f"\nDownload Completed Successfully! Video saved at: {download_path}")
    except Exception as e:
        print(f"\nDownload Failed! Error: {str(e)}")

if __name__ == "__main__":
    link = input("Enter your YouTube link: ")

    # Specify the current directory as the default save path
    save_path = os.getcwd()

    Downloader(link, save_path)
