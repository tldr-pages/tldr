# popeye

> A Kubernetes telepítési manifesztekkel kapcsolatos lehetséges problémákat jelző segédprogram. További információ: <https://github.com/derailed/popeye>.

- Az aktuális Kubernetes fürt átvizsgálása:

`popeye`

- Egy adott névtér átvizsgálása:

`popeye -n {{namespace}}`

- Egy adott Kubernetes-kontextus átvizsgálása:

`popeye --context={{context}}`

- Spencer konfigurációs fájl használata a szkenneléshez:

`popeye -f {{spinach.yaml}}`
