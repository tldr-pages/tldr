# htpdate

> Synchronize local date and time via HTTP headers from web servers.
> More information: <http://www.vervest.org/htp/>.

- Synchronize date and time:

`sudo htpdate {{host}}`

- Perform simulation of syncronization, without any action:

`htpdate -q {{host}}`

- Compensate the systematisch clock drift:

`sudo htpdate -x {{host}}`

- Set time immediate after the syncronization:

`sudo htpdate -s {{host}}`
