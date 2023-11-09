# choco-push

> Push a compiled nupkg to a package feed.
> More information: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push a compiled nupkg to the specified feed:

`choco push --source {{https://push.chocolatey.org/}}`

- Try to push a compiled nupkg to the specified feed before hitting the timeout:

`choco push --source {{"'https://push.chocolatey.org/'"}} --execution-timeout {{500}}`
