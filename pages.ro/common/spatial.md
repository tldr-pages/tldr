# spatial

> Un set de comenzi pentru gestionarea și dezvoltarea proiectelor SpatialOS.

- Rulați acest lucru atunci când utilizați un proiect pentru prima dată:

`spatial worker build`

- Construiți lucrători pentru implementare locală pe Unity pe macOS:

`spatial worker build --target=development --target=Osx`

- Construiți lucrători pentru implementarea locală pe Unreal pe Windows:

`spatial worker build --target=local --target=Windows`

- Implementaţi local:

`spatial local launch {{launch_config}} --snapshot={{snapshot_file}}`

- Lansați un lucrător local pentru a vă conecta la implementarea locală:

`spatial local worker launch {{worker_type}} {{launch_config}}`

- Încărcați un ansamblu de utilizat pentru implementări în cloud:

`spatial cloud upload {{assembly_name}}`

- Lansarea unei implementări în cloud:

`spatial cloud launch {{assembly_name}} {{launch_config}} {{deployment_name}}`

- Directoare pentru lucrători curaţi:

`spatial worker clean`
