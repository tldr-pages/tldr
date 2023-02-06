# glab pipeline

> A GitLab CI/CD pipelines listázása, megtekintése és futtatása. További információk: <https://glab.readthedocs.io/en/latest/pipeline>.

- Egy futó csővezeték megtekintése az aktuális ágon:

`glab pipeline status`

- Egy adott ágon futó csővezeték megtekintése:

`glab pipeline status --branch {{branch_name}}`

- A csővezetékek listájának lekérdezése:

`glab pipeline list`

- Kézi csővezeték futtatása az aktuális ágon:

`glab pipeline run`

- Kézi csővezeték futtatása egy adott ágon:

`glab pipeline run --branch {{branch_name}}`
