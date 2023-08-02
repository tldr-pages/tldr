# mkhomedir_helper

> Create the user home folder after creating the user.
> More information: <https://manned.org/mkhomedir_helper.8>.

- Create a home folder for a user based on /etc/skel with umask 022:

`sudo mkhomedir_helper {{user_name}}`
