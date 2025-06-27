# gdebi

> Easily install `.deb` files.
> More information: <https://manned.org/gdebi>.

- Install local `.deb` packages resolving and installing its dependencies:

`gdebi {{path/to/package.deb}}`

- Do not show progress information:

`gdebi {{path/to/package.deb}} {{[-q|--quiet]}}`

- Set an APT configuration option:

`gdebi {{path/to/package.deb}} {{[-o|--option]}} {{APT_OPTS}}`

- Use alternative root dir:

`gdebi {{path/to/package.deb}} --root {{path/to/root_dir}}`

- Display version:

`gdebi --version`
