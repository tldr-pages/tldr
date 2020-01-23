# fls

> List files and directories in an image file or device.
> More information at https://wiki.sleuthkit.org/index.php?title=Fls

- Built a recursive fls list over a device:

`fls -r -m {{Original_Path}} {{/dev/examplepartition}}`

- The above, for a partition starting at a specific sector using a pre-defined timezone:

`fls -r -m {{Original_Path}} -z {{timezone}} -o {{sector}} {{imagefile}}`

- Create a timeline of filesystem changes in ASCII CSV format

`fls -r -m {{Original_Path}} -z {{timezone}} -o {{sector}} {{imagefile}} | mactime -d -z {{timezone}} > {{outputfile}}`
