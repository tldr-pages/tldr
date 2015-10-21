# transcode

> Suite of command line utilities for transcoding video and audio codecs
> and converting between formats.

- Remove camera shaking and convert to MPEG4 (using xvid). The first command

    creates a transformation-file that is needed for stabilization. The second
    command then transforms the video using xvid.

```
transcode -J stabilize -i {{inputfile}}`
transcode -J transform -i {{inputfile}} -y xvid -o {{outputfile}}
```

- Resize the video to 640x480 Pixels and convert to MPEG4 codec using xvid.

`transcode -Z 640x480 -i {{inputfile}} -y xvid -o {{outputfile}}`
