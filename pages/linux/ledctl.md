# ledctl

> Intel(R) Enclosure LED Control Application.
> More information: <https://manned.org/ledctl>.

- Turn on the "Locate" LED for specified device(s):

`sudo ledctl locate={{/dev/sda,/dev/sdb,...}}`

- Turn off the "Locate" LED for specified device(s):

`sudo ledctl locate_off={{/dev/sda,/dev/sdb,...}}`

- Turn off the "Status" LED and "Failure" LED for specified device(s):

`sudo ledctl off={{/dev/sda,/dev/sdb,...}}`

- Turn off the "Status" LED, "Failure" LED and "Locate" LED for specified device(s):

`sudo ledctl normal={{/dev/sda,/dev/sdb,...}}`
