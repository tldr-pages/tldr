# fly

> Parancssori eszköz a concourse-ci számára. További információ: <https://concourse-ci.org/fly.html>.

- Hitelesítés és mentés a concourse target segítségével:

`fly --target {{target_name}} login --team-name {{team_name}} -c {{https://ci.example.com}}`

- Célpontok listázása:

`fly targets`

- Pipelines listázása:

`fly -t {{target_name}} pipelines`

- Pipeline feltöltése vagy frissítése:

`fly -t {{target_name}} set-pipeline --config {{pipeline.yml}} --pipeline {{pipeline_name}}`

- Csővezeték szüneteltetésének feloldása:

`fly -t {{target_name}} unpause-pipeline --pipeline {{pipeline_name}}`

- Csővezeték-konfiguráció megjelenítése:

`fly -t {{target_name}} get-pipeline --pipeline {{pipeline_name}}`

- A fly helyi példányának frissítése:

`fly -t {{target_name}} sync`

- Csővezeték megsemmisítése:

`fly -t {{target_name}} destroy-pipeline --pipeline {{pipeline_name}}`
