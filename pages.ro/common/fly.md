# fly

> Instrument de linie de comandă pentru concurse-ci.
> Mai multe informaţii: <https://concourse-ci.org/fly.html>

- Autentificare cu și de a salva țintă:

`fly --target {{target_name}} login --team-name {{team_name}} -c {{https://ci.example.com}}`

- Lista obiectivelor:

`fly targets`

- Lista conductelor:

`fly -t {{target_name}} pipelines`

- Încărcați sau actualizați o conductă:

`fly -t {{target_name}} set-pipeline --config {{pipeline.yml}} --pipeline {{pipeline_name}}`

- Conductă neîntreruptă:

`fly -t {{target_name}} unpause-pipeline --pipeline {{pipeline_name}}`

- Afișează configurația conductei:

`fly -t {{target_name}} get-pipeline --pipeline {{pipeline_name}}`

- Actualizați copia locală a zborului:

`fly -t {{target_name}} sync`

- Distruge conducta:

`fly -t {{target_name}} destroy-pipeline --pipeline {{pipeline_name}}`
