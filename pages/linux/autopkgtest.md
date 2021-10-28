# autopkgtest

> Run tests on Debian packages.
> More information: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Build the package in the current directory and run all tests using the `null` virtualization server:

`autopkgtest -- null`

- Run a specific test for the package in the current directory:

`autopkgtest --test-name={{test}} -- null`

- Download the given package, build it, and run all tests:

`autopkgtest {{package}} -- null`

- Test the package inside the given chroot:

`autopkgtest -- chroot {{path/to/chroot}}`

- Test the package without rebuilding it:

`autopkgtest --no-built-binaries -- null`
