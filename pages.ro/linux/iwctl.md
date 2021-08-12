# iwctl

> Un instrument de linie de comandă pentru controlul solicitantului de rețea iwd.
> Mai multe informaţii: <https://iwd.wiki.kernel.org/gettingstarted>

- Porniți modul interactiv, în acest mod puteți introduce comenzile direct, cu autocompletare:

`iwctl`

- Sună la ajutor general:

`iwctl --help`

- Afișați stațiile WiFi:

`iwctl station list`

- Începeți să căutați rețele cu o stație:

`iwctl station {{station}} scan`

- Afișează rețelele găsite de o stație:

`iwctl station {{station}} get-networks`

- Conectați-vă la o rețea cu o stație, dacă sunt necesare acreditări, li se va cere:

`iwctl station {{station}} connect {{network_name}}`
