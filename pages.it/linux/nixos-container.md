# nixos-container

> Avvia container NixOS usando container Linux.
> Maggiori informazioni: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Elenca i container in esecuzione:

`sudo nixos-container list`

- Crea un container NixOS con un file di configurazione specifico:

`sudo nixos-container create {{nome_container}} --config-file {{percorso_file_configurazione_nix}}`

- Avvia, ferma, termina o elimina uno specifico container:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{nome_container}}`

- Esegue un comando all'interno di un container in esecuzione:

`sudo nixos-container run {{nome_container}} -- {{comando}} {{argomenti}}`

- Aggiorna la configurazione di un container:

`sudo $EDITOR /var/lib/container/{{nome_container}}/etc/nixos/configuration.nix && sudo nixos-container update {{nome_container}}`

- Entra in una sessione shell interattiva in un container già in esecuzione:

`sudo nixos-container root-login {{nome_container}}`
