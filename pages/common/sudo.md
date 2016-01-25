# sudo

> Execute a command as another user.

- List of an unreadable directory:

`sudo {{ls}} {{/usr/local/scrt}}`

- To edit a file as user www:

`sudo -u {{www}} {{vi}} {{/var/www/index.html}}`

- To shutdown the machine:

`sudo {{shutdown}} -r +10 {{"Cya soon!"}}`

- To repeat the last command as sudo:

`sudo {{!!}}`
