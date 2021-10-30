# unshadow

> Utility provided by the John the Ripper project to obtain the traditional Unix password file if the system uses shadow passwords.
> More information: <https://www.openwall.com/john/>.

- Combine the `/etc/shadow` and `/etc/passwd` of the current system:

`sudo unshadow /etc/passwd /etc/shadow`

- Combine two arbitrary shadow and password files:

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`
