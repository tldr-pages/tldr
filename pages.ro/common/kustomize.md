# kustomize

> Kustomize este un instrument pentru a implementa cu ușurință resurse pentru Kubernetes.
> Mai multe informaţii: <https://github.com/kubernetes-sigs/kustomize>

- Creați fișierul kustomization cu resurse și spațiu de nume:

`kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}`

- Construiți fișierul kustomization și implementați-l cu `kubectl`:

`kustomize build . | kubectl apply -f -`

- Setați o imagine în fișierul kustomization:

`kustomize edit set image {{busybox=alpine:3.6}}`

- Căutați resurse Kubernetes în directorul curent care urmează să fie adăugate la fișierul kustomization:

`kustomize create --autodetect`
