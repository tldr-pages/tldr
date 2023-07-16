# ffplay

> A simple and portable media player using the FFmpeg libraries and the SDL library.
> More information: <https://ffmpeg.org/ffplay-all.html>.

- Play a media file:

`ffplay {{path/to/file}}`

- Play audio from a media file without a GUI:

`ffplay -nodisp {{path/to/file}}`

- Play media passed by `ffmpeg` through `stdin`:

`ffmpeg -i {{path/to/file}} -c {{copy}} -f {{media_format}} - | ffplay -`

- Play a video and show motion vectors in real time:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{path/to/file}}`

- Show only video keyframes:

`ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{path/to/file}}`
