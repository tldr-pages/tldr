# gpu-screen-recorder

> Record the screen and encode the video with a GPU.
> More information: <https://git.dec05eba.com/gpu-screen-recorder/about/>.

- Select a source using a desktop portal and record it:

`gpu-screen-recorder -w portal -o {{path/to/video.mp4}}`

- Specify a specific video source:

`gpu-screen-recorder -w {{screen|DP-1|HDMI-A1|...}} -o {{path/to/video.mp4}}`

- List video capture sources:

`gpu-screen-recorder --list-capture-options`

- List audio capture sources:

`gpu-screen-recorder {{--list-audio-devices|--list-application-audio}}`

- Record using the replay buffer:

`gpu-screen-recorder -w {{screen}} -r {{30}} -c {{mp4}} -ro {{path/to/directory}} -o {{whatever}}`

- Capture a video from the replay buffer:

`pkill -SIGUSR1 -f gpu-screen-recorder`

- Run `gpu-screen-recorder` in the background:

`systemctl start --user gpu-screen-recorder`
