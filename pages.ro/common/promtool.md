# promtool

> Instrumente pentru sistemul de monitorizare Prometeu.
> Mai multe informaţii: <https://prometheus.io/docs/prometheus/latest/getting_started/>

- Verificați dacă fișierele de configurare sunt valide sau nu (dacă prezintă erori de raport):

`promtool check config {{config_file.yml}}`

- Verificați dacă fișierele de regulă sunt valide sau nu (dacă există erori de raport):

`promtool check rules {{rules_file.yml}}`

- Treceți măsurătorile Prometeu peste stdin pentru a le verifica pentru coerență și corectitudine:

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- Testele unitare pentru reguli de configurare:

`promtool test rules {{test_file.yml}}`
