# lvm_import_vdo

> Importa un volume VDO creato dal gestore VDO in un volume logico gestito da LVM (irreversibile).
> Maggiori informazioni: <https://manned.org/lvm_import_vdo>.

- Importa un volume VDO con nomi automatici per VG/LV:

`lvm_import_vdo {{/dev/mapper/vdo_volume}}`

- Importa e imposta il nome di destinazione VG/LV:

`lvm_import_vdo {{[-n|--name]}} {{vg_name/lv_name}} {{/dev/mapper/vdo_volume}}`

- Mostra cosa verrebbe fatto senza modificare nulla:

`lvm_import_vdo --dry-run {{/dev/mapper/vdo_volume}}`

- Converti sul posto senza usare uno snapshot temporaneo (meno sicuro):

`lvm_import_vdo --no-snapshot {{/dev/mapper/vdo_volume}}`

- Output dettagliato e rispondi automaticamente "sì" ai prompt:

`lvm_import_vdo {{[-v|--verbose]}} {{[-y|--yes]}} {{/dev/mapper/vdo_volume}}`

- Usa un file di configurazione del gestore VDO durante l'importazione:

`lvm_import_vdo --vdo-config {{path/to/vdo.conf}} {{/dev/mapper/vdo_volume}}`
