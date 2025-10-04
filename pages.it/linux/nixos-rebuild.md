# nixos-rebuild

> Riconfigura una macchina NixOS.
> Maggiori informazioni: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Compila e passa alla nuova configurazione, rendendola quella predefinita all'avvio:

`sudo nixos-rebuild switch`

- Compila e passa alla nuova configurazione, rendendola quella predefinita all'avvio e assegnando un nome alla voce del menù di avvio:

`sudo nixos-rebuild switch {{[-p|--profile-name]}} {{nome}}`

- Compila e passa alla nuova configurazione, rendendola quella predefinita all'avvio e installando gli aggiornamenti:

`sudo nixos-rebuild switch --upgrade`

- Annulla le modifiche alla configurazione, passando alla generazione precedente:

`sudo nixos-rebuild switch --rollback`

- Compila la nuova configurazione rendendola quella predefinita all'avvio, senza passare ad essa:

`sudo nixos-rebuild boot`

- Compila e passa alla nuova configurazione senza aggiungere la voce al menù di avvio (a scopo di test):

`sudo nixos-rebuild test`

- Compila la configurazione e la apre in una macchina virtuale:

`sudo nixos-rebuild build-vm`

- Elenca le generazioni disponibili in modo simile al menù di avvio:

`nixos-rebuild list-generations`
