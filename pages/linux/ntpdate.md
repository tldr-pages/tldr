# ntpdate

> Synchronize and set the date and time via NTP.
> More information: <http://support.ntp.org/documentation>.

- Synchronize and set date and time:

`sudo ntpdate {{host}}`

- Query the host without setting the time:

`ntpdate -q {{host}}`

- Use an unprivileged port in case a firewall is blocking privileged ports:

`sudo ntpdate -u {{host}}`

- Force time to be stepped using `settimeofday` instead of `slewed`:

`sudo ntpdate -b {{host}}`
