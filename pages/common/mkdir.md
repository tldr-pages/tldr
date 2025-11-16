# mkdir

> Create directories and set their permissions.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Create specific directories:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Create specific directories and their parents if needed:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- Create directories with specific permissions:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`

- Create multiple nested directories recursively:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`

- Create a directory with specific permissions (e.g., rwxr-xr-x):

`mkdir --mode={{755}} {{directory_name}}`
