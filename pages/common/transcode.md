# transcode

> Video stream processing tool that can change size of video or remove shaking
> and more

- Create transformation file (to remove camera shaking).

`transcode -J stabilize -i {{inputfile}}`

- Remove camera shaking (needs transformation file from step above).

`transcode -J transform -i {{inputfile}} -y xvid -o {{outputfile}}`

- Video resizing

`transcode -Z 640x480 -i {{inputfile}} -y xvid -o {{outputfile}}`
