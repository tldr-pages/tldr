# singularity

> Manage Singularity containers and images.

- Download a remote image from Sylabs Cloud:

`singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}`

- Rebuild a remote image using latest Singularity image format:

`singularity build {{image.sif}} {{docker://godlovedc/lolcow}}`

- Start a container from an image and get a shell inside of it:

`singularity shell {{image.sif}}`

- Start a container from an image and run a command:

`singularity exec {{image.sif}} {{command}}`

- Start a container from an image and execute the internal runscript:

`singularity run {{image.sif}}`

- Build a singularity image from a recipe file:

`sudo singularity build {{image.sif}} {{recipe}}`
