# fls

> List files and directories in an image file or device.
> More information: <https://wiki.sleuthkit.org/index.php?title=Fls>.

- Build a recursive fls list over a device:

`fls -r -m {{original_path}} {{/dev/examplepartition}}`

- Analyse a single partition, providing the timezone of the original system and the sector offset at which the file system starts in the image:

`fls -r -m {{original_path}} -z {{timezone}} -o {{sector}} {{imagefile}}`

- Create a timeline of filesystem changes in ASCII CSV format:

`fls -r -m {{original_path}} -z {{timezone}} -o {{sector}} {{imagefile}} | mactime -d -z {{timezone}} > {{outputfile}}`
