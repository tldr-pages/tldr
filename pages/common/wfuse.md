# wfuse

> Mount Wii and GameCube images or WBFS files and partitions using FUSE.
> More information: <https://wit.wiimm.de/wfuse/>.

- Mount a Wii or GameCube image to a directory:

`wfuse {{path/to/image.wdf}} {{path/to/mount_point}}`

- Mount a WBFS file to a directory:

`wfuse {{path/to/file.wbfs}} {{path/to/mount_point}}`

- Create the mount point if it does not exist:

`wfuse --create {{path/to/image.iso}} {{path/to/mount_point}}`

- Unmount a mounted image:

`wfuse --umount {{path/to/mount_point}}`

- Unmount lazily:

`wfuse --lazy --umount {{path/to/mount_point}}`

- Remount an image by first unmounting an existing mount:

`wfuse --remount {{path/to/image.iso}} {{path/to/mount_point}}`

- Display help:

`wfuse --help`

- Display version information:

`wfuse --version`
