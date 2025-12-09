# autopkgtest

> Run tests on Debian packages.
> More information: <https://manpages.debian.org/bookworm/autopkgtest/autopkgtest.1.en.html>.

- Build the package in the current directory and run all tests directly on the system:

`autopkgtest -- {{null}}`

- Run a specific test for the package in the current directory:

`autopkgtest --test-name={{test_name}} -- {{null}}`

- Download and build a specific package with `apt-get`, then run all tests:

`autopkgtest {{package}} -- {{null}}`

- Test the package in the current directory using a new root directory:

`autopkgtest -- {{chroot}} {{path/to/new_root}}`

- Test the package in the current directory without rebuilding it:

`autopkgtest {{[-B|--no-built-binaries]}} -- {{null}}`
