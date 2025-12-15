# lvmpersist

> Gestisce le prenotazioni persistenti (PR) su dispositivi di blocco o tutti i PV in un volume group.
> Maggiori informazioni: <https://manned.org/lvmpersist>.

- Avvia PR su tutti i PV in un VG con chiave locale (accesso esclusivo per impostazione predefinita):

`lvmpersist start --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- Avvia PR per un VG condiviso (permette più host):

`lvmpersist start --ourkey {{0x1234abcd}} --access {{sh}} --vg {{vg_name}}`

- Ferma PR su un VG e deregistra la chiave locale:

`lvmpersist stop --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- Prende il controllo di un VG locale premettendo un altro host durante l'avvio PR:

`lvmpersist start --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- Rimuove la chiave di un altro host da un VG condiviso:

`lvmpersist remove --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- Mostra chiavi registrate e prenotazioni per un VG:

`lvmpersist read --vg {{vg_name}}`

- Opera su dispositivi specifici invece di un VG:

`lvmpersist start --ourkey {{0x1234abcd}} --device {{/dev/sdX}} --device {{/dev/mapper/mpathY}}`
