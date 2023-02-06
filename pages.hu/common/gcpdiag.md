# gcpdiag

> Google Cloud Platform hibaelhárító és diagnosztikai eszköz. Docker konténerben vagy GCP Cloudshellben futtatható. További információk: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- Futtassa a `gcpdiag` oldalt a projektjén, és adja vissza az összes szabályt:

`gcpdiag lint --project={{gcp_project_id}}`

- Rejtse el azokat a szabályokat, amelyek rendben vannak:

`gcpdiag lint --project={{gcp_project_id}} --hide-ok`

- Hitelesítés a szolgáltatási fiók privát kulcsfájljának használatával:

`gcpdiag lint --project={{gcp_project_id}} --auth-key {{path/to/private_key}}`

- Naplók és mérőszámok keresése több napra visszamenőleg (alapértelmezett: 3 nap):

`gcpdiag lint --project={{gcp_project_id}} --within-days {{number}}`

- Súgó megjelenítése:

`gcpdiag lint --help`
