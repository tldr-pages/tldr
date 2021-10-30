# mp4box

> MPEG-4 Systems Toolbox - Muxes streams into MP4 container.
> More information: <https://gpac.wp.imt.fr/mp4box>.

- Display information about an existing MP4 file:

`mp4box -info {{filename}}`

- Add an SRT subtitle file into an MP4 file:

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Combine audio from one file and video from another:

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`
