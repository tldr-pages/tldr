# useradd

> Add a new user or edit default user configuation

- Create a user using the current default configuration

`sudo useradd {{username}}`

- Create a user in the specified group with the specified home directory path

`sudo useradd -g {{group}} -d {{/path/to/home/}} {{username}}`

- Create user and copy files from `/skel/dir` to user's home directory

`sudo useradd -k {{/skel/dir}} {{username}}`

- Display the current default user configuration values

`sudo useradd -D`

- Change the default home directory prefix, group, and shell for new users

`sudo useradd -D -b {{/home/prefix}} -g {{group}} -s {{shell}}`

