# hyprctl

> Steuere Teile des Hyprland Wayland-Compositors.
> Weitere Informationen: <https://wiki.hypr.land/Configuring/Advanced-and-Cool/Using-hyprctl/>.

- Lade die Hyprland-Konfiguration neu:

`hyprctl reload`

- Gib den Namen das aktiven Fensters zurück:

`hyprctl activewindow`

- Zeige eine Liste aller verbundenen Eingabegeräte:

`hyprctl devices`

- Zeige eine Liste aller Ausgänge mit ihren jeweiligen Eigenschaften:

`hyprctl workspaces`

- Rufe einen Dispatcher auf:

`hyprctl dispatch {{dispatcher}}`

- Setzte ein Konfigurations-Schlüsselwort dynamisch:

`hyprctl keyword {{keyword}} {{value}}`

- Zeige die Version:

`hyprctl version`
