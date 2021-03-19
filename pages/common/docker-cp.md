# docker cp

> Copy files or directories between host and container filesystems.
> More information: <https://docs.docker.com/engine/reference/commandline/cp>.

- Copy a file or directory from the host to a container:

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Copy a file or directory from a container to the host:

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Copy a file or directory from the host to a container, following symlinks (copies the symlinked files directly, not the symlinks themselves):

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
