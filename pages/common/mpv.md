# mpv

> A audio/video player based on MPlayer.
> More information: <https://mpv.io>.

- Play a video or audio file:

`mpv {{file}}`

- Jump backward/forward 5 seconds:

`LEFT <or> RIGHT`

- Jump backward/forward 1 minute:

`DOWN <or> UP`

- Decrease or increase playback speed by 10 %:

`[ <or> ]`

- Play a file at a specified speed (0.01 to 100, default 1):

`mpv --speed {{speed}} {{file}}`

- Play a file using a profile defined in the `mpv.conf` file:

`mpv --profile {{profile_name}} {{file}}`
