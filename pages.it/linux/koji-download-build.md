# koji download-build

> Scarica un pacchetto compilato.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Scarica tutti gli RPM da una build specifica:

`koji download-build {{BuildID|RPM|NVR}}`

- Scarica gli RPM firmati con la chiave data:

`koji download-build {{BuildID|RPM|NVR}} --key {{chiave}}`

- Scarica solo gli RPM per una data architettura:

`koji download-build {{BuildID|RPM|NVR}} --arch {{x86_64,aarch64,noarch,...}}`

- Scarica l'RPM specificato:

`koji download-build {{RPM}} --rpm`

- Mostra aiuto:

`koji download-build {{[-h|--help]}}`
