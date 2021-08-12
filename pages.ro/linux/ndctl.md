# ndctl

> Utilitar pentru gestionarea DIMM-urilor non-volatile.

- Creați un spațiu de nume de mod 'fsdax':

`ndctl create-namespace --mode={{fsdax}}`

- Modificați modul unui spațiu de nume la „raw”:

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- Verificați un spațiu de nume al modului sector pentru consistență și reparați dacă este necesar:

`ndctl check-namespace --repair {{namespaceX.Y}}`

- Listați toate spațiile de nume, regiunile și autobuzele (inclusiv cele cu handicap):

`ndctl list --namespaces --regions --buses --idle`

- Listați un anumit spațiu de nume și includeți o mulțime de informații suplimentare:

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- Rulați un monitor pentru a viziona pentru evenimente de sănătate SMART pentru NVDIMM pe magistrala „ACPI.NFIT”:

`ndctl monitor --bus={{ACPI.NFIT}}`

- Eliminați un spațiu de nume (dacă este cazul) sau resetați-l la o stare inițială:

`ndctl destroy-namespace --force {{namespaceX.Y}}`
