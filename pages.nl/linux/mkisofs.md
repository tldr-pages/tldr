# mkisofs

> Maak ISO-bestanden van mappen.
> Ook bekend als alias `genisoimage`.
> Meer informatie: <https://manned.org/mkisofs>.

- Maak een ISO van een map:

`mkisofs -o {{bestandsnaam.iso}} {{pad/naar/bron_map}}`

- Stel het schijflabel in tijdens het maken van een ISO:

`mkisofs -o {{bestandsnaam.iso}} -V "{{label_naam}}" {{pad/naar/bron_map}}`

- Maak een ISO-image met bestanden groter dan 2GiB door een kleinere schijnbare grootte te rapporteren voor ISO9660-bestandssystemen:

`mkisofs -o {{bestandsnaam.iso}} -allow-limited-size {{pad/naar/bron_map}}`
