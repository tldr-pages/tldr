# automount

> Read the `/etc/auto_master` file and mount `autofs` on the appropriate mount points to trigger the on-demand mounting of directories. Essentially, it's a way to manually initiate the system's automounting process.
> Note: You'll most likely need to run with `sudo` if you don't have the necessary permissions.
> More information: <https://keith.github.io/xcode-man-pages/automount.8.html>.

- Run automount, flush the [c]ache beforehand, and be [v]erbose about it (most common use):

`automount -cv`

- Automatically unmount after 5 minutes (300 seconds) of inactivity:

`automount -t 300`

- [u]nmount anything previously mounted by automount and/or defined in `/etc/auto_master`:

`automount -u`
