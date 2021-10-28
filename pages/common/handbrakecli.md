# handbrakecli

> Command-line interface to the HandBrake video conversion and DVD ripping tool.
> More information: <https://handbrake.fr/>.

- Convert a video file to MKV (AAC 160kbit audio and x264 CRF20 video):

`handbrakecli --input {{input.avi}} --output {{output.mkv}} --encoder x264 --quality 20 --ab 160`

- Resize a video file to 320x240:

`handbrakecli --input {{input.mp4}} --output {{output.mp4}} --width 320 --height 240`

- List available presets:

`handbrakecli --preset-list`

- Convert an AVI video to MP4 using the Android preset:

`handbrakecli --preset="Android" --input {{input.ext}} --output {{output.mp4}}`

- Print the content of a DVD, getting the CSS keys in the process:

`handbrakecli --input {{/dev/sr0}} --title 0`

- Rip the first track of a DVD in the specified device. Audiotracks and subtitle languages are specified as lists:

`handbrakecli --input {{/dev/sr0}} --title 1 --output {{out.mkv}} --format av_mkv --encoder x264 --subtitle {{1,4,5}} --audio {{1,2}} --aencoder copy --quality {{23}}`
