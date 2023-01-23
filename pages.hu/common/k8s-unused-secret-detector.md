# k8s-unused-secret-detector

> Parancssoros eszköz a fel nem használt Kubernetes-titkok felderítésére. További információ: <https://github.com/dtan4/k8s-unused-secret-detector>.

- Fel nem használt titkok felderítése:

`k8s-unused-secret-detector`

- A fel nem használt titkok felderítése egy adott névtérben:

`k8s-unused-secret-detector -n {{namespace}}`

- Fel nem használt titkok törlése egy adott névtérben:

`k8s-unused-secret-detector -n {{namespace}} | kubectl delete secret -n {{namespace}}`
