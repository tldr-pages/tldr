# nomad

> Programarea distribuită, foarte disponibilă, conștientă de centrul de date.
> Mai multe informaţii: <https://www.nomadproject.io/docs/commands/>

- Arată starea nodurilor din cluster:

`nomad node status`

- Validează un fișier de locuri de muncă:

`nomad job validate {{path/to/file.nomad}}`

- Planificați un loc de muncă pentru execuție pe cluster:

`nomad job plan {{path/to/file.nomad}}`

- Rulați un loc de muncă pe cluster:

`nomad job run {{path/to/file.nomad}}`

- Arată starea de locuri de muncă care rulează în prezent pe cluster:

`nomad job status`

- Afișați informațiile detaliate despre starea unui anumit loc de muncă:

`nomad job status {{job_name}}`

- Urmați jurnalele unei alocări specifice:

`nomad alloc logs {{alloc_id}}`

- Afișați starea volumelor de stocare:

`nomad volume status`
