# autopkgtest

> Run tests on Debian packages.
> More information: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Build the package in the current directory and run all tests directly on the system:

`autopkgtest -- {{null}}`

- Run a specific test for the package in the current directory:

`autopkgtest --test-name={{test_name}} -- {{null}}`

- Download and build a specific package with `apt-get`, then run all tests:

`autopkgtest {{package}} -- {{null}}`

- Test the package in the current directory using a new root directory:

`autopkgtest -- {{chroot}} {{path/to/new/root}}`

- Test the package in the current directory without rebuilding it:

`autopkgtest --no-built-binaries -- {{null}}`
