# salt

> Execută comenzi și afirmă starea minionilor de sare de la distanță.
> Mai multe informaţii: <https://docs.saltstack.com/ref/cli/salt.html>

- Lista minionilor conectați:

`salt '*' test.ping`

- Execută un highstate pe toți minionii conectați:

`salt '*' state.highstate`

- Upgrade pachete folosind managerul de pachete OS (apt, yum, brew) pe un subset de minioni:

`salt '*.example.com' pkg.upgrade`

- Execută o comandă arbitrară asupra unui anumit minion:

`salt '{{minion_id}}' cmd.run "ls "`
