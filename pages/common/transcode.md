# transcode

> Suite of command line utilities for transcoding video and audio codecs
> and converting between formats.

- Remove camera shaking and convert to MPEG4 (using xvid).
- First create file used to stabilize.
- Now transform the original video using xvid.

`transcode -J stabilize -i {{inputfile}}`
`transcode -J transform -i {{inputfile}} -y xvid -o {{outputfile}}`

- Resize the video to 640x480 Pixels and convert to MPEG4 codec using xvid.

`transcode -Z 640x480 -i {{inputfile}} -y xvid -o {{outputfile}}`
