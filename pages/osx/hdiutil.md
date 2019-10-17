# hdiutil

> Utility to create and manage disk images.

- Mount an image:

`hdiutil attach {{filename}}`

- Unmount an image:

`hdiutil detach /Volumes/{{volumename}}`

- List mounted images:

`hdiutil info`

- Create an ISO image from the contents of a directory:

`hdiutil makehybrid -o {{filename}} {{dirname}}`
