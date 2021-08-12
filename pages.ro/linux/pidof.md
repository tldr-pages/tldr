# pidof

> Primește ID-ul unui proces utilizând numele acestuia.

- Listează toate ID-urile de proces cu numele dat:

`pidof {{bash}}`

- Listați un singur ID de proces cu numele dat:

`pidof -s {{bash}}`

- Lista ID-urilor de proces, inclusiv script-uri cu nume dat:

`pidof -x {{script.py}}`

- Ucide toate procesele cu numele dat:

`kill "$(pidof {{name}})" `
