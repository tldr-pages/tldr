# satis

> Utilitarul de linie de comandă pentru depozitul static Compozitor Satis.
> Mai multe informaţii: <https://github.com/composer/satis>

- Iniţializarea unei configuraţii Satis:

`satis init {{satis.json}}`

- Adăugați un depozit VCS la configurația Satis:

`satis add {{repository_url}}`

- Construiți ieșirea statică din configurație:

`satis build {{satis.json}} {{path/to/output_directory}}`

- Construiți ieșirea statică prin actualizarea numai a depozitului specificat:

`satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}`

- Eliminați fișierele de arhivă inutile:

`satis purge {{satis.json}} {{path/to/output_directory}}`
