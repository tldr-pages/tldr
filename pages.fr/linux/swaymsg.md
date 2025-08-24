# swaymsg

> Communique avec Sway, gestionnaire de fenêtres en mosaïque (tiling).
> Plus d'informations : <https://manned.org/man/swaymsg>.

- Liste les identifiants des périphèriques d'entrée (clavier, souris, …) (voir <https://github.com/swaywm/sway/wiki#input-configuration>) :

`swaymsg --pretty --type get_inputs | grep --after-context=2 'Input device'`

- Liste les identifiants des périphèriques de sortie (écrans connectés, …) (voir <https://github.com/swaywm/sway/wiki#display-configuration>, <https://gitlab.freedesktop.org/emersion/kanshi>) :

`swaymsg --pretty --type get_outputs | grep --after-context=1 '^Output'`

- Liste les espaces de travail de Sway, et leurs états :

`swaymsg --type get_workspaces`

- Liste toutes les fenêtres, conteneurs, périphèriques de sorties, espaces de travail, … Cela aide à identifier les critères pour les commandes `assign` (voir <https://manned.org/man/sway.5>) :

`swaymsg --type get_tree`

- Affiche la configuration active de Sway. Ne développe pas les inclusions :

`swaymsg --type get_config`

- Affiche la configuration de swaybar au format JSON (voir <https://manned.org/man/sway-bar>) :

`swaymsg --type get_bar_config`
