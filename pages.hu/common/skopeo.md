# skopeo

> Konténerkép-kezelő eszköztár. Különböző segédparancsokat biztosít a távoli konténerképek kezeléséhez. További információ: <https://github.com/containers/skopeo>.

- Távoli kép ellenőrzése a nyilvántartásból:

`skopeo inspect docker://{{registry_hostname}}/{{image:tag}}`

- Listázza a távoli kép elérhető címkéit:

`skopeo list-tags docker://{{registry_hostname}}/{{image}}`

- Kép letöltése egy regiszterből:

`skopeo copy docker://{{registry_hostname}}/{{image:tag}} dir:{{path/to/directory}}`

- Képmásolás egy regiszterből egy másikba:

`skopeo copy docker://{{source_registry}}/{{image:tag}} docker://{{destination_registry}}/{{image:tag}}`

- Kép törlése egy regiszterből:

`skopeo delete docker://{{registry_hostname}}/{{image:tag}}`

- Bejelentkezés egy kibocsátásiegység-forgalmi jegyzékbe:

`skopeo login --username {{username}} {{registry_hostname}}`
