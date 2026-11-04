# svcadm

> Manipulate service instances.
> More information: <https://www.unix.com/man-page/sunos/1m/svcadm>.

- Enable a service in the service database:

`svcadm enable {{service_name}}`

- Disable a service:

`svcadm disable {{service_name}}`

- Restart a running service:

`svcadm restart {{service_name}}`

- Make a service re-read its configuration files:

`svcadm refresh {{service_name}}`

- Clear a service from maintenance state and command it to start:

`svcadm clear {{service_name}}`
