# promtool

> Eszközök a Prometheus monitoring rendszerhez. További információ: <https://prometheus.io/docs/prometheus/latest/getting_started/>.

- Ellenőrizze, hogy a konfigurációs fájlok érvényesek-e vagy sem (ha vannak, hibát jelent):

`promtool check config {{config_file.yml}}`

- Ellenőrizze, hogy a szabályfájlok érvényesek-e vagy sem (ha vannak, hibákat jelent):

`promtool check rules {{rules_file.yml}}`

- Prometheus metrikák átadása a `stdin` oldalon, hogy ellenőrizze azok konzisztenciáját és helyességét:

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- Egységtesztek a szabályok konfigurációjához:

`promtool test rules {{test_file.yml}}`
