# kompose

> Un instrument pentru conversia aplicațiilor docker-compun în Kubernetes.
> Mai multe informaţii: <https://github.com/kubernetes/kompose>

- Implementați o aplicație dockerized la Kubernetes:

`kompose up -f {{docker-compose.yml}}`

- Ștergeți serviciile/implementările instanțiate din Kubernetes:

`kompose down -f {{docker-compose.yml}}`

- Conversia unui fișier docker-compunere în fișierul de resurse Kubernetes:

`kompose convert -f {{docker-compose.yml}}`
