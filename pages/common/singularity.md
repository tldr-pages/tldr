# singularity

> Manage Singularity containers and images.

- Download a remote image:

`singularity pull --name {{container.simg}} {{shub://vsoch/hello-world}}`

- Rebuild a remote image using latest Singularity image format:

`singularity build {{container.simg}} {{docker://godlovedc/lolcow}}`

- Start a container from an image and get a shell inside of it:

`singularity shell {{container.simg}}`

- Start a container from an image and run a command:

`singularity exec {{container.simg}} {{command}}`

- Start a container from an image and execute the internal runscript:

`singularity run {{container.simg}}`

- Build a singularity image from a recipe file:

`sudo singularity build {{container.simg}} {{recipe}}`
