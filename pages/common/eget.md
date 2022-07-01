# eget

> Easily install prebuilt binaries from GitHub.
> More information: <https://github.com/zyedidia/eget>.

- Download a prebuilt binary for the current system from a repository on GitHub:

`eget {{zyedidia/micro}}`

- Download from a URL:

`eget {{https://go.dev/dl/go1.17.5.linux-amd64.tar.gz}}`

- Specify the location to place the downloaded files:

`eget {{zyedidia/micro}} --to={{path/to/directory}}`

- Specify a `git` tag instead of using the latest version:

`eget {{zyedidia/micro}} --tag={{v2.0.10}}`

- Install the latest pre-release instead of the latest stable version:

`eget {{zyedidia/micro}} --pre-release`

- Only download the asset, skipping extraction:

`eget {{zyedidia/micro}} --download-only`

- Only download if there is a newer release then the currently downloaded version:

`eget {{zyedidia/micro}} --upgrade-only`
