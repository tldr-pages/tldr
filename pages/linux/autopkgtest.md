# autopkgtest

> Run tests on Debian packages.
> More information: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Build the package in the current directory and run all tests using the `null` virtualization server:

`autopkgtest -- null`

- Run a specific test for the package in the current directory:

`autopkgtest --test-name={{testname}} -- null`

- Download and build a specific package, then run all tests:

`autopkgtest {{package}} -- null`

- Test the package in the current directory using a new root directory:

`autopkgtest -- chroot {{path/to/new/root}}`

- Test the package without rebuilding it:

`autopkgtest --no-built-binaries -- null`
