# hdiutil

> Utility to create and manage disk images.
> More information: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Mount an image:

`hdiutil attach {{path/to/image_file}}`

- Unmount an image:

`hdiutil detach /Volumes/{{volume_file}}`

- List mounted images:

`hdiutil info`

- Create an ISO image from the contents of a directory:

`hdiutil makehybrid -o {{path/to/output_file}} {{path/to/directory}}`
