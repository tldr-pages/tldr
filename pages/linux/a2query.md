# a2query

> Retrieve runtime configuration from Apache on Debian-based OSes.
> More information: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- List enabled Apache modules:

`sudo a2query -m`

- Check if a specific module is installed:

`sudo a2query -m {{module_name}}`

- List enabled virtual hosts:

`sudo a2query -s`

- Display the currently enabled Multi Processing Module:

`sudo a2query -M`

- Display the Apache version:

`sudo a2query -v`
