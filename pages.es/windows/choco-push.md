# choco-push

> Sube un paquete NuGet compilado (`nupkg`) a un feed de paquetes.
> Más información: <https://docs.chocolatey.org/en-us/create/commands/push>.

- Subir un `nupkg` compilado al feed especificado:

`choco push --source {{https://push.chocolatey.org/}}`

- Subir un `nupkg` compilado al feed especificado con un tiempo de espera en segundos (el valor predeterminado es 2700):

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`
