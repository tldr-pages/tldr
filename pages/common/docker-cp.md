# docker cp

> Copy files/directories between host and container filesystems.
> More information: <https://docs.docker.com/engine/reference/commandline/cp/>.

- Copy from the host into a container:

`docker cp {{path/to/file_or_directory/on/host}} {{container_name}}:{{path/to/file_or_directory/in/container}}`

- Copy from a container onto the host:

`docker cp {{container_name}}:{{path/to/file_or_directory/in/container}} {{path/to/file_or_directory/on/host}}`
