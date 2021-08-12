# salt-call

> Invocați sare local pe un minion de sare.
> Mai multe informaţii: <https://docs.saltstack.com/ref/cli/salt-call.html>

- Efectuați un highstate pe acest minion:

`salt-call state.highstate`

- Efectuați o executare uscată de înaltă stare, calculați toate modificările, dar nu le efectuați de fapt:

`salt-call state.highstate test=true`

- Efectuați un highstate cu ieșire de depanare verbose:

`salt-call -l debug state.highstate`

- Listează boabele acestui minion:

`salt-call grains.items`
