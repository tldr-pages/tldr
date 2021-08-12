# syncthing

> Instrument de sincronizare descentralizată continuă a dosarelor bidirecționale.
> Mai multe informaţii: <https://docs.syncthing.net/>

- Începe sincronizarea:

`syncthing`

- Începeți sincronizarea fără a deschide un browser web:

`syncthing -no-browser`

- Imprimați ID-ul dispozitivului:

`syncthing -device-id`

- Schimbă directorul de acasă:

`syncthing -home={{path/to/directory}}`

- Forțați un schimb complet de indici:

`syncthing -reset-deltas`

- Schimbați adresa pe care interfața web ascultă:

`syncthing -gui-address={{ip_address:port|path/to/socket.sock}}`

- Arată căile de fișiere la fișierele utilizate de sincronizare:

`syncthing -paths`

- Dezactivați procesul de sincronizare a monitorului:

`syncthing -no-restart`
