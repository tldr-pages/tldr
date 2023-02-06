# gitlab

> Ruby wrapper és CLI a GitLab API-hoz. Néhány alparancsnak, mint például a `gitlab ctl`, saját használati dokumentációja van. További információ: <https://narkoz.github.io/gitlab/>.

- Hozzon létre egy új projektet:

`gitlab create_project {{project_name}}`

- Információ lekérése egy adott commitról:

`gitlab commit {{project_name}} {{commit_hash}}`

- Információ lekérése a CI csővezetékben lévő munkákról:

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- Egy adott CI-munka elindítása:

`gitlab job_play {{project_name}} {{job_id}}`
