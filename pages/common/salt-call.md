# salt-call

> Invoke salt locally on a salt minion.
> More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>.

- Perform a highstate on this minion:

`salt-call state.highstate`

- Simulate a highstate, computing all changes without actually performing them:

`salt-call state.highstate test=true`

- Perform a highstate with verbose debugging output:

`salt-call {{[-l|--log-level]}} debug state.highstate`

- List this minion's grains:

`salt-call grains.items`
