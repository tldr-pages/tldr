# kompose

> Eszköz a docker-compose alkalmazások Kubernetesbe való konvertálásához. További információ: <https://github.com/kubernetes/kompose>.

- Dockerizált alkalmazás telepítése a Kubernetesbe:

`kompose up -f {{docker-compose.yml}}`

- A Kubernetesből instanciált szolgáltatások/telepítések törlése:

`kompose down -f {{docker-compose.yml}}`

- A docker-compose fájl konvertálása Kubernetes erőforrás-fájlba:

`kompose convert -f {{docker-compose.yml}}`
