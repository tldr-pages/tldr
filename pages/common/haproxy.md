# haproxy

> Fast and reliable HTTP reverse proxy and load balancer.
> More information: <https://manned.org/haproxy>.

- Check configuration file for validity:

`haproxy -c -f {{path/to/haproxy.cfg}}`

- Start HAProxy with a configuration file:

`haproxy -f {{path/to/haproxy.cfg}}`

- Start in daemon mode:

`haproxy -D -f {{path/to/haproxy.cfg}}`

- Start in master-worker mode:

`haproxy -W -f {{path/to/haproxy.cfg}}`

- Start with debugging mode enabled (foreground, verbose output):

`haproxy -d -f {{path/to/haproxy.cfg}}`

- Reload configuration with graceful shutdown of old process:

`haproxy -f {{path/to/haproxy.cfg}} -sf {{pid}}`

- Set maximum number of simultaneous connections:

`haproxy -f {{path/to/haproxy.cfg}} -n {{maxconn}}`

- Reload with zero downtime by reusing sockets from old process:

`haproxy -f {{path/to/haproxy.cfg}} -x {{/var/run/haproxy.sock}} -sf {{pid}}`
