# htpdate

> Synchronize local date and time via HTTP headers from web servers.
> Requires administrator privileges.
> More information: <http://www.vervest.org/htp/>.

- Synchronize date and time:

`htpdate {{host}}`

- Perform simulation of syncronization, without any action:

`htpdate -q {{host}}`

- Compensate the systematisch clock drift:

`htpdate -x {{host}}`

- Set time immediate after the syncronization:

`htpdate -s {{host}}`
