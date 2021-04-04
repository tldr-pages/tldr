# handbrakecli

> Command-line interface to the HandBrake video conversion tool.
> More information: <https://handbrake.fr/>.

- Convert a video file to MKV (AAC 160kbit audio and x264 CRF20 video):

`handbrakecli -i {{input.avi}} -o {{output.mkv}} -e x264 -q 20 -B 160`

- Resize a video file to 320x240:

`handbrakecli -i {{input.mp4}} -o {{output.mp4}} -w 320 -l 240`

- List available presets:

`handbrakecli --preset-list`

- Convert an AVI video to MP4 using the Android preset:

`handbrakecli --preset="Android" -i {{input.ext}} -o {{output.mp4}}`
