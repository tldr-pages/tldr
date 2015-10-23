# HandBrakeCLI

> Video conversion tool

- Convert a video file to MKV (AAC 160kbit audio and x264 CRF20 video)

`HandBrakeCLI -i {{input.avi}} -o {{output.mkv}} -e x264 -q 20 -B 160`

- Resize a video file to 320x240

`HandBrakeCLI -i {{input.mp4}} -o {{output.mp4} -w 320 -l 240`

- List available presets

`HandBrakeCLI --preset-list`

- Convert an AVI video to MP4 using the Android preset

`HandBrakeCLI --preset="Android" -i {{input.ext}} -o {{output.mp4}}`
