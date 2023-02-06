# yq

> Könnyű és hordozható parancssori YAML-feldolgozó. További információ: <https://mikefarah.gitbook.io/yq/>.

- YAML fájl kimenete, pretty-print formátumban (v4+):

`yq eval {{path/to/file.yaml}}`

- YAML fájl kimenete, pretty-print formátumban (v3):

`yq read {{path/to/file.yaml}} --colors`

- Egy olyan YAML-fájl első elemének kiadása, amely csak egy tömböt tartalmaz (v4+):

`yq eval '.[0]' {{path/to/file.yaml}}`

- Egy olyan YAML-fájl első elemének kiadása, amely csak egy tömböt tartalmaz (v3):

`yq read {{path/to/file.yaml}} '[0]'`

- Egy kulcs beállítása (vagy felülírása) egy fájlban lévő értékre (v4+):

`yq eval '.{{key}} = "{{value}}"' --inplace {{path/to/file.yaml}}`

- Egy kulcs beállítása (vagy felülírása) egy fájlban lévő értékre (v3):

`yq write --inplace {{path/to/file.yaml}} '{{key}}' '{{value}}'`

- Két fájl egyesítése és nyomtatás a `stdout` címre (v4+):

`yq eval-all 'select(filename == "{{path/to/file1.yaml}}") * select(filename == "{{path/to/file2.yaml}}")' {{path/to/file1.yaml}} {{path/to/file2.yaml}}`

- Két fájl egyesítése és nyomtatása a `stdout` címre (v3):

`yq merge {{path/to/file1.yaml}} {{path/to/file2.yaml}} --colors`
