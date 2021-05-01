# newusers

> Update and create new users in batch mode.
> More information: <https://manned.org/useradd>.

- It reads from a file with the following format:

`<username>:<passwd>:<uid>:<gid>:<user_info>:<home_dir>:<default_shell>`

- Create users.txt file and add account details (Multiple entries allowed):

`ozzy:Linmaster1:1003:1003:Admin User:/home/ozzy:bin/bash`

- Set required permissions:

`chmod 600 users.txt`

- Run with input file:

`{{newusers}} users.txt`
