from moviepy.editor import VideoFileClip
import tempfile


def extract_audio(video_path):

    temp_audio = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    video = VideoFileClip(video_path)

    audio = video.audio

    audio.write_audiofile(
        temp_audio.name,
        codec="pcm_s16le"
    )

    audio.close()
    video.close()

    return temp_audio.name