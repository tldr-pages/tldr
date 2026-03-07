# hyprpaper

> Wallpaper utility for Hyprland with the ability to dynamically change wallpapers.
> Controlled by the config file `~/.config/hypr/hyprpaper.conf`.
> More information: <https://github.com/hyprwm/hyprpaper>.

- Start the hyprpaper service:

`hyprpaper`

- Change wallpaper for a specific monitor:

`hyprctl hyprpaper wallpaper "{{monitor}},{{path/to/image.png}}"`

- Change wallpaper to a given image, tiling it across all monitors:

`hyprctl hyprpaper wallpaper ",{{path/to/image.png}},tile"`
