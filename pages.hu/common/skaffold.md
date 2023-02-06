# skaffold

> A Kubernetes alkalmazások folyamatos fejlesztését megkönnyítő eszköz. További információ: <https://skaffold.dev>.

- Építse meg a leletek:

`skaffold build -f {{skaffold.yaml}}`

- Építse és telepítse az alkalmazást minden alkalommal, amikor a kódja változik:

`skaffold dev -f {{skaffold.yaml}}`

- Futtasson egy csővezetékfájlt:

`skaffold run -f {{skaffold.yaml}}`

- Futtasson diagnosztikát a Skaffoldon:

`skaffold diagnose -f {{skaffold.yaml}}`

- Deploy the artifacts:

`skaffold deploy -f {{skaffold.yaml}}`
