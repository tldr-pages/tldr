# copr-cli

> Interface met Fedora-projecten copr instantie voor het bouwen van RPM's en het publiceren ervan.
> Meer informatie: <https://manned.org/copr-cli>.

- Toon de gebruiker ingelogd in copr:

`copr-cli whoami`

- Bouw een lokaal spec-bestand op copr:

`copr-cli build {{repository}} {{pad/naar/spec_bestand}}`

- Controleer de status van de builds:

`copr-cli list-builds {{repository}}`

- Trigger een copr build van een spec-bestand vanuit een publieke (Git) repository:repository:

`copr-cli buildscm {{repository}} --clone-url {{https://git.example.org/repo}} --spec {{spec_bestandsnaam}}`
