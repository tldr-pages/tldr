# choco-push

> Push een gecompileerd NuGet pakket (`nupkg`) naar een pakketfeed.
> Meer informatie: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Push een gecompileerd `nupkg` naar de gespecificeerde feed:

`choco push --source {{https://push.chocolatey.org/}}`

- Push een gecompileerd `nupkg` naar de gespecificeerde feed met een timeout in seconden (standaard is 2700):

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`
