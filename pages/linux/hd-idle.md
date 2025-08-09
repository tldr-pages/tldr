# hd-idle

> Utility program for spinning-down external disks after a period of idle time.
> More information: <https://hd-idle.sourceforge.net/>.

- There needs to be a service running for auto-spin down. By default hard disks will spin down after 10 minutes of inactivity:

`/etc/init.d/hd-idle start`

- Spin down a disk immediately:

`hd-idle -t sda`

- Set idle time to 0 (meaning hd-idle will never try to spin down a disk), then set explicit idle times (in seconds) for disks which have the string "sda" or "sdb" in their device name (sda to spin down after 5 min of inactivity, sdb - after 20 min):

`hd-idle -i 0 -a sda -i 300 -a sdb -i 1200`
