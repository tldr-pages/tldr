# ntpd

> The official NTP (Network Time Protocol) daemon to synchronize the system clock to remote time servers or local reference clocks.
> More information: <https://www.ntp.org/documentation/4.2.8-series/ntpd/>.

- Start the daemon:

`sudo ntpd`
- Synchronize system time with remote servers a single time (quit after synchronizing):

`sudo ntpd --quit`

- Synchronize a single time allowing "Big" adjustments:

`sudo ntpd --panicgate --quit`
