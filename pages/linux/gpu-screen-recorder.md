# gpu-screen-recorder

> Record the screen and encode the video with a GPU.
> More information: <https://git.dec05eba.com/gpu-screen-recorder/about/>.

- Select a source using a desktop portal and record it:

`gpu-screen-recorder -w portal -o {{path/to/video.mp4}}`

- Specify a specific source:

`gpu-screen-recorder -w {{screen|DP-1|HDMI-A1|...}} -o {{path/to/video.mp4}}`

- List capture sources:

`gpu-screen-recorder --list-capture-options`
