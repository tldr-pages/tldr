# fluxctl

> Parancssori eszköz a Flux v1-hez. További információ: <https://fluxcd.io/legacy/flux/references/fluxctl>.

- A fürtben jelenleg futó munkaterhelések listázása egy adott névtérben:

`fluxctl --k8s-fwd-ns={{namespace}} list-workloads`

- Telepített és elérhető képek megjelenítése:

`fluxctl list-images`

- A fürt szinkronizálása a git-tárral:

`fluxctl sync`

- Automatikus telepítés bekapcsolása egy munkaterheléshez:

`fluxctl automate`
