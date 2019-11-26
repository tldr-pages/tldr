# a2dissite

> Disable an Apache virtual host on Debian-based OSes.
> More information: <https://manpages.debian.org/buster/apache2/a2dissite.8.en.html>.

- Disable a virtual host:

`sudo a2dissite {{virtual_host}}`

- Don't show informative messages:

`sudo a2dissite --quiet {{virtual_host}}`
