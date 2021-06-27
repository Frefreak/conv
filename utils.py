import os
import ffmpeg


root_dir = os.path.abspath(os.path.dirname(__file__))
bin_dir = os.path.join(root_dir, "bin")
ffmpeg_cmd = os.path.join(bin_dir, "ffmpeg.exe")


def conv_audio_mp3(fp):
    output = os.path.join(os.path.splitext(fp)[0] + ".mp3")
    stream = ffmpeg.input(fp)
    stream = ffmpeg.output(stream, output)
    r, err = ffmpeg.run(stream, cmd=ffmpeg_cmd, overwrite_output=True)
    return output, err
