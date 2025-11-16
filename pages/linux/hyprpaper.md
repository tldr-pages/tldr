# hyprpaper

> Wallpaper utility for Hyprland with the ability to dynamically change wallpapers through sockets.
> Controlled by the config file ~/.config/hypr/hyprpaper.conf.
> More information: <https://github.com/hyprwm/hyprpaper>.

- Start the hyprpaper service:

`hyprpaper`

- Switch wallpaper to a different preloaded image:

`hyprctl hyprpaper wallpaper "{{display}},{{path/to/image.png}}"`

- List the wallpapers that are currently preloaded (useful for dynamically preloading and unloading):

`hyprctl hyprpaper listloaded`

- List the active wallpapers hyprpaper is displaying, along with its associated monitor:

`hyprctl hyprpaper listactive`
