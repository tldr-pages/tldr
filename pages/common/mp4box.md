# MP4Box

> MPEG-4 Systems Toolbox - Muxes streams into MP4 container.

- Display information about an existing MP4 file:

`MP4Box -info {{filename}}`

- Add an SRT subtitle file into an MP4 file:

`MP4Box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Combine audio from one file and video from another:

`MP4Box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}`
