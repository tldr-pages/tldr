# wit

> Wiimms ISO Tool for manipulating Wii and GameCube disc images.
> More information: <https://wit.wiimm.de/wit/>.

- List all found ISO files:

`wit LIST {{path/to/image_or_directory}}`

- Display detailed information about an ISO image:

`wit DUMP {{path/to/image.iso}}`

- Extract all files from an ISO image to a directory:

`wit EXTRACT {{path/to/image.iso}} {{path/to/output_directory}}`

- Copy an image while converting it to WDF:

`wit COPY {{path/to/input.iso}} --dest {{path/to/output.wdf}}`

- Convert an image to WIA with a specified compression mode:

`wit COPY {{path/to/input.iso}} --wia --compression {{compression_mode}} --dest {{path/to/output.wia}}`

- Verify an ISO image by calculating and comparing its SHA1 checksums:

`wit VERIFY {{path/to/image.iso}}`

- Display help:

`wit --help`
