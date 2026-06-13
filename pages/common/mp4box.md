# mp4box

> MPEG-4 Systems Toolbox: muxe streams into MP4 container.
> More information: <https://github.com/gpac/gpac/wiki/Fragmentation,-segmentation,-splitting-and-interleaving>.

- Display information about an existing MP4 file:

`mp4box -info {{path/to/file}}`

- Add an SRT subtitle file into an MP4 file:

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- Combine audio from one file and video from another:

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`
