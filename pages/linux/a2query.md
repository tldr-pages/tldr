# a2query

> Retrieve runtime configuration from Apache on Debian-based OSes.
> More information: <https://manned.org/a2query>.

- List enabled Apache modules:

`sudo a2query -m`

- Check if a specific module is installed:

`sudo a2query -m {{module_name}}`

- List enabled virtual hosts:

`sudo a2query -s`

- Display the currently enabled Multi Processing Module:

`sudo a2query -M`

- Display Apache version:

`sudo a2query -v`
