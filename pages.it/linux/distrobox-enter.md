# distrobox-enter

> Entra in un container Distrobox.
> Il comando predefinito eseguito è la tua `$SHELL`, ma puoi specificare shell diverse o interi comandi da eseguire. Se usato dentro uno script, un'applicazione o un servizio, puoi usare la modalità `--headless` per disabilitare il tty e l'interattività.
> Vedi anche: `distrobox`.
> Maggiori informazioni: <https://distrobox.it/usage/distrobox-enter/>.

- Entra in un container Distrobox:

`distrobox-enter {{container_name}}`

- Entra in un container Distrobox ed esegui un comando al login:

`distrobox-enter {{container_name}} -- {{sh -l}}`

- Entra in un container Distrobox senza istanziare un tty:

`distrobox-enter {{[-n|--name]}} {{container_name}} -- {{uptime --pretty}}`
