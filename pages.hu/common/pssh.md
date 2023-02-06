# pssh

> Párhuzamos SSH program. További információ: <https://manned.org/pssh>.

- Futtasson egy parancsot két hoszton, és a kimenetét mindkét szerveren sorban kiírja:

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- Futtasson egy parancsot, és mentse a kimenetet külön fájlba:

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{hostname -i}}`

- Futtasson egy parancsot több hoszton, új sorral elválasztott fájlban megadva:

`pssh -i -h {{path/to/hosts_file}} {{hostname -i}}`

- Egy parancs futtatása root-ként (ez a root jelszót kéri):

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{hostname -i}}`

- Parancs futtatása további SSH-argumentumokkal:

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- A párhuzamos kapcsolatok számát 10-re korlátozó parancs futtatása:

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
