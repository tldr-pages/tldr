# keychain

> re-use ssh-agent and/or gpg-agent between logins
> More information: <http://funtoo.org/Keychain>.

- Check for a running ssh-agent, and start one if needed:

`keychain`

- Also check for gpg-agent:

`keychain --agents "gpg,ssh"`

- List signatures of all active keys and exit:

`keychain --list`

- List fingerprints of all active keys and exit:

`keychain --list-fp`

- Add a timeout for identities added to the agent, in minutes:

`keychain --timeout {{minutes}}`

- Enforce using gpg2 over gpg (for distributions like Ubuntu that have both)

`keychain --gpg2`
