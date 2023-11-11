# choco-push

> Push a compiled NuGet package (`nupkg`) to a package feed.
> More information: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push a compiled `nupkg` to the specified feed:

`choco push --source {{https://push.chocolatey.org/}}`

- Push a compiled `nupkg` to the specified feed with a timeout in seconds (default is 2700):

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`
