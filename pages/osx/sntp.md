# sntp

> A very Simple Network Time Protocol client program.

- Query the SNTP server `pool.ntp.org` and display the time:

`sntp {{pool.ntp.org}}`

- Synchronize the system clock with the SNTP server at `pool.ntp.org`:

`sudo sntp -S {{pool.ntp.org}}`

- Enable debug logging:

`sntp -d {{pool.ntp.org}}`
