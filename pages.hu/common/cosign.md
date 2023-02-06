# cosign

> Konténerek aláírása, ellenőrzése és tárolása egy OCI-nyilvántartásban. További információ: <https://github.com/sigstore/cosign>.

- Kulcspár generálása:

`cosign generate-key-pair`

- A konténer aláírása és az aláírás tárolása a nyilvántartásban:

`cosign sign -key {{cosign.key}} {{image}}`

- Egy konténerkép aláírása egy Kubernetes-titokban tárolt kulcspárral:

`cosign sign -key k8s://{{namespace}}/{{key}} {{image}}`

- Írjon alá egy blobot egy helyi kulcspárfájllal:

`cosign sign-blob --key {{cosign.key}} {{path/to/file}}`

- Ellenőrizzen egy konténert egy nyilvános kulcs ellenében:

`cosign verify -key {{cosign.pub}} {{image}}`

- Képek hitelesítése egy Dockerfile-ban lévő nyilvános kulccsal:

`cosign dockerfile verify -key {{cosign.pub}} {{path/to/Dockerfile}}`

- Egy kép hitelesítése egy Kubernetes-titkban tárolt nyilvános kulccsal:

`cosign verify -key k8s://{{namespace}}/{{key}} {{image}}`

- Egy konténerkép és az aláírások másolása:

`cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}`
