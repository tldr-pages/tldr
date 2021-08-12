# gitlab

> Ambalaj Ruby și CLI pentru API-ul GitLab.
> Mai multe informaţii: <https://narkoz.github.io/gitlab/>

- Creați un nou proiect:

`gitlab create_project {{project_name}}`

- Obțineți informații despre un anumit angajament:

`gitlab commit {{project_name}} {{commit_hash}}`

- Obțineți informații despre locurile de muncă într-o conductă de CI:

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- Începeți un loc de muncă specific CI:

`gitlab job_play {{project_name}} {{job_id}}`
