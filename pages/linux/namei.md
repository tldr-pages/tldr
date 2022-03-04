# namei

> Follows a pathname (which can be a symbolic link) until a terminal point is found (a file/directory/char device etc).
> This program is useful for finding "too many levels of symbolic links" problems.
> More information: <https://manned.org/namei>.

- Resolve the pathnames specified as the argument parameters:

`namei {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Display the results in a long-listing format:

`namei --long {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Show the mode bits of each file type in the style of `ls`:

`namei --modes {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Show owner and group name of each file:

`namei --owners {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Don't follow symlinks while resolving:

`namei --nosymlinks {{path/to/a}} {{path/to/b}} {{path/to/c}}`
