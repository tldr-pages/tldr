# ndc

> Name daemon control service for name servers.
> If a command isn't provided, NDC will prompt for one until EOF.
> More information: <https://manned.org/ndc>.

- Set the [c]ontrol channel rendezvous point:

`ndc -c {{channel}} {{command}}`

- Bind the client side to a specific [l]ocalsock address:

`ndc -l {{localsock}} {{command}}`

- Set path to [p]idfile for UNIX signal control:

`ndc -p {{path/to/pidfile}} {{command}}`

- Enable [d]ebugging:

`ndc -d {{command}}`

- Enable [q]uiet mode:

`ndc -q {{command}}`

- Enable nonfatal error [s]uppression:

`ndc -s {{command}}`

- Enable [t]racing for protocol and system debugging:

`ndc -t {{command}}`

- List built-in commands:

`ndc /help`
