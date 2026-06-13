# lynis

> System and security auditing tool.
> More information: <https://cisofy.com/documentation/lynis/>.

- Check that Lynis is up-to-date:

`sudo lynis update info`

- Run a security audit of the system:

`sudo lynis audit system`

- Run a security audit of a Dockerfile:

`sudo lynis audit dockerfile {{path/to/dockerfile}}`
