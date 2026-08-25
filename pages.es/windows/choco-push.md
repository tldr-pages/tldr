# choco push

> Sube un paquete NuGet compilado (`.nupkg`) a un feed de paquetes.
> Más información: <https://docs.chocolatey.org/en-us/create/commands/push/>.

- Sube un `.nupkg` compilado al feed especificado:

`choco push {{[-s|--source]}} {{https://push.chocolatey.org/}}`

- Sube un `.nupkg` compilado al feed especificado con un tiempo de espera en segundos (el valor predeterminado es 2700):

`choco push {{[-s|--source]}} {{https://push.chocolatey.org/}} {{[--timeout|--execution-timeout]}} {{500}}`
