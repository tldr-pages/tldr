# nordvpn

> Kommandozeilen-Schnittstelle für NordVPN.
> Weitere Informationen: <https://support.nordvpn.com/hc/en-us/articles/20196094470929-Installing-NordVPN-on-Linux-distributions>.

- Interaktiv bei einem NordVPN-Konto anmelden:

`nordvpn login`

- Zeige den Verbindungsstatus an:

`nordvpn status`

- Stelle eine Verbindung zum nächsten NordVPN-Server her:

`nordvpn connect`

- Liste alle verfügbaren Länder auf:

`nordvpn countries`

- Stelle eine Verbindung zu einem NordVPN-Server in einem bestimmten Land her:

`nordvpn connect {{Germany}}`

- Stelle eine Verbindung zu einem NordVPN-Server in einem bestimmten Land und einer bestimmten Stadt her:

`nordvpn connect {{Germany}} {{Berlin}}`

- Aktiviere die `autoconnect`-Option:

`nordvpn set autoconnect on`
