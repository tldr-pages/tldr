# consul-kv

> Rete distribuita per gestire e configurare servizi tramite database chiave-valore.

- Leggi il valore di una chiave da un database chiave-valore:

`consul kv get {{chiave}}`

- Memorizza una nuova coppia chiave-valore:

`consul kv put {{chiave}} {{valore}}`

- Elimina una coppia chiave-valore:

`consul kv delete {{chiave}}`
