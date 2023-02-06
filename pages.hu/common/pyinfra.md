# pyinfra

> Automatizálja az infrastruktúrát nagy léptékben. További információ: <https://docs.pyinfra.com>.

- Parancs végrehajtása SSH-n keresztül:

`pyinfra {{target_ip_address}} exec -- {{command_name_and_arguments}}`

- Egy telepítési fájl tartalmának végrehajtása a célpontok listáján:

`pyinfra {{path/to/target_list.py}} {{path/to/deploy.py}}`

- Parancsok végrehajtása helyben:

`pyinfra @local {{path/to/deploy.py}}`

- Parancsok végrehajtása a Dockeren keresztül:

`pyinfra @docker/{{container}} {{path/to/deploy.py}}`
