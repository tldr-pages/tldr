# fio

> Rugalmas I/O tesztelő. Eszköz, amely számos szálat vagy folyamatot indít egy adott típusú I/O művelet elvégzésére. További információ: <https://fio.readthedocs.io/en/latest/fio_doc.html>.

- Véletlenszerű olvasások tesztelése:

`sudo fio --filename={{path/to/file}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Szekvenciális olvasások tesztelése:

`sudo fio --filename={{path/to/file}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Véletlenszerű olvasás/írás tesztelése:

`sudo fio --filename={{path/to/file}} --size=500GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1`

- Tesztelés feladatfájlból származó paraméterekkel:

`sudo fio {{path/to/job_file}}`

- Egy adott munkafájl átalakítása parancssori opciókká:

`fio --showcmd {{path/to/job_file}}`
