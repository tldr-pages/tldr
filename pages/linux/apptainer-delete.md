# apptainer delete

> Delete container images from a remote library.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_delete.html>.

- Delete an image from the Container Library:

`apptainer delete library://{{user/collection/container}}:{{tag}}`

- Delete an image for a specific architecture:

`apptainer delete --arch {{amd64|arm64|ppc64le}} library://{{user/collection/container}}:{{tag}}`

- [F]orce delete an image without confirmation:

`apptainer delete {{[-F|--force]}} library://{{user/collection/container}}:{{tag}}`

- Delete an image from a specific library server:

`apptainer delete --library {{https://library.example.com}} library://{{user/collection/container}}:{{tag}}`

- Delete an image using HTTP instead of HTTPS:

`apptainer delete --no-https library://{{hostname/user/collection/container}}:{{tag}}`

- Display help:

`apptainer delete {{[-h|--help]}}`
