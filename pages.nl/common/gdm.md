# gdm

> De GNOME Display Manager (GDM) is een vervanging voor de X Display Manager (XDM).
> Zie ook: `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`.
> Meer informatie: <https://manned.org/gdm>.

- Voer de GNOME Display Manager-applicatie uit:

`gdm`

- Voorkom dat `gdm` als een daemon achtergrondproces wordt uitgevoerd:

`gdm --nodaemon`

- Schakel `gdm`-beheer van lokale console X servers uit voor headless of externe omgevingen:

`gdm --no-console`

- Voorkom het opschonen van omgevingsvariabelen die beginnen met `LD_`:

`gdm --preserve-ld-vars`

- Toon de help:

`gdm --help`

- Toon de versie:

`gdm --version`
