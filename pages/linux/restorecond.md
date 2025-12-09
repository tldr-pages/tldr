# restorecond

> Daemon that monitors file creation and automatically restores SELinux contexts.
> Useful for directories where files are frequently created with incorrect contexts.
> See also: `restorecon`, `semanage-fcontext`.
> More information: <https://manned.org/restorecond>.

- Start the `restorecond` daemon:

`sudo restorecond`

- Run `restorecond` in [v]erbose mode to see restoration events:

`sudo restorecond -v`

- Run `restorecond` in [d]ebug mode:

`sudo restorecond -d`

- Use alternative restorecond.conf file:

`sudo restorecond -f restorecond_file`

- Check the status of the restorecond service:

`sudo systemctl status restorecond`

- Enable restorecond to start at boot:

`sudo systemctl enable restorecond --now`
