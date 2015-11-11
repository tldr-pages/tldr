# transcode

> Suite of command line utilities for transcoding video and audio codecs
> and converting between formats.

- Create stabilisation file to be able to remove camera shakes.

`transcode -J stabilize -i {{inputfile}}`

- Remove camera shakes after creating stabilisation file, transform video using xvid.

`transcode -J transform -i {{inputfile}} -y xvid -o {{outputfile}}`

- Resize the video to 640x480 Pixels and convert to MPEG4 codec using xvid.

`transcode -Z 640x480 -i {{inputfile}} -y xvid -o {{outputfile}}`
