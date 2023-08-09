# mkhomedir_helper

> Create the user home folder after creating the user.
> More information: <https://manned.org/mkhomedir_helper>.

- Create a home directory for a user based on `/etc/skel` with umask 022:

`sudo mkhomedir_helper {{username}}`

- Create a home folder for a user based on /etc/skel with all permissions for owner (0) and read permission for group (3):

`sudo mkhomedir_helper {{user_name}} {{037}}`

- Create a home folder for a user based on a custom skeleton location:

`sudo mkhomedir_helper {{user_name}} {{umask}} {{path/to/folder}}`
