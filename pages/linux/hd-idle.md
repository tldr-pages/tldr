# hd-idle

> Spin down external disks after a period of idle time.
> More information: <https://manned.org/hd-idle>.

- Start a service to manage hard drive spin down. By default hard disks will spin down after 10 minutes of inactivity:

`systemctl start hd-idle`

- Spin down a disk immediately:

`hd-idle -t {{/dev/sdX}}`

- Set disks to never spin down, then set explicit idle times (in seconds) for disks which have "sda" or "sdb" in their device name:

`hd-idle -i 0 -a /dev/sda -i {{300}} -a /dev/sdb -i {{1200}}`
