# wait4x tcp

> Wait for TCP port(s) to become available.
> More information: <https://github.com/wait4x/wait4x>.

- Wait for a TCP port to become available:

`wait4x tcp {{localhost:8080}}`

- Wait for a port with a specific timeout:

`wait4x tcp {{localhost:3306}} --timeout {{60s}}`

- Wait for a port to become free (inverted check):

`wait4x tcp {{localhost:8080}} --invert-check`

- Wait for multiple ports in parallel:

`wait4x tcp {{localhost:3306 localhost:6379 ...}}`

- Run a command after the port becomes available:

`wait4x tcp {{localhost:3306}} -- {{path/to/script.sh}}`

- Wait with exponential backoff:

`wait4x tcp {{localhost:8080}} --backoff-policy exponential --backoff-exponential-max-interval {{30s}}`
