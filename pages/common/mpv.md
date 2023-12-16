# mpv

> A audio/video player based on MPlayer.
> More information: <https://mpv.io>.

- Play a video or audio from a URL or file:

`mpv {{url|path/to/file}}'`

- Jump backward/forward 5 seconds:

`LEFT <or> RIGHT`

- Jump backward/forward 1 minute:

`DOWN <or> UP`

- Decrease or increase playback speed by 10%:

`[ <or> ]`

- Take a screenshot of the current frame (saved to `./mpv-shotNNNN.jpg` by default):

`s`

- Play a file at a specified speed (1 by default):

`mpv --speed {{0.01..100}} {{path/to/file}}`

- Play a file using a profile defined in the `mpv.conf` file:

`mpv --profile {{profile_name}} {{path/to/file}}`

- Display the output of webcam or other video input device:

`mpv /dev/{{video0}}`
