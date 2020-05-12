> Utility provided by the package "john", to combine /etc/passwd and /etc/shadow into a file that can be processed by John the Ripper. More information: <https://www.openwall.com/john/>.

- Combine the /etc/shadow and /etc/passwd of the current system:

`unshadow /etc/passwd /etc/shadow`

- Combine two arbitrary shadow and password files:

`unshadow {{/path/to/passwd}} {{/path/to/shadow}}`
