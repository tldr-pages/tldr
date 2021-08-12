# k8s-unused-secret-detector

> instrument de interfață linie de comandă pentru detectarea secretelor Kubernetes neutilizate.
> Mai multe informaţii: <https://github.com/dtan4/k8s-unused-secret-detector>

- Detectați secretele neutilizate:

`k8s-unused-secret-detector`

- Detectați secretele neutilizate într-un anumit spațiu de nume:

`k8s-unused-secret-detector -n {{namespace}}`

- Ștergeți secretele neutilizate într-un anumit spațiu de nume:

`k8s-unused-secret-detector -n {{namespace}} | kubectl delete secret -n {{namespace}}`
