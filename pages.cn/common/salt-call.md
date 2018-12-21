# salt-key

> Invoke salt locally on a salt minion.

- Perform a highstate on this minion:

`salt-call state.highstate`

- Perform a highstate dry-run, compute all changes but don't actually perform them:

`salt-call state.highstate test=true`

- Perform a highstate with verbose debugging output:

`salt-call -l debug state.highstate`

- List this minion's grains:

`salt-call grains.items`
