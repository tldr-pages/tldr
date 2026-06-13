# nixos-option

> Ispeziona una configurazione NixOS.
> Maggiori informazioni: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Elenca tutte le sottochiavi di una data opzione:

`nixos-option {{opzione}}`

- Elenca tutti i moduli del kernel corrente:

`nixos-option boot.kernelModules`

- Elenca le chiavi di autorizzazioni per uno specifico utente:

`nixos-option users.users.{{utente}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- Elenca tutte le macchine di compilazione remote:

`nixos-option nix.buildMachines`

- Elenca tutte le sottochiavi di una data opzione di un'altra configurazione NixOS:

`NIXOS_CONFIG={{percorso_per_configuration.nix}} nixos-option {{opzione}}`

- Visualizza ricorsivamente tutti i valori per un utente:

`nixos-option {{[-r|--recursive]}} users.users.{{utente}}`
