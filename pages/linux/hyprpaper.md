# hyprpaper

> Wallpaper utility for Hyprland with the ability to dynamically change wallpapers.
> Controlled by the config file `~/.config/hypr/hyprpaper.conf`.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprpaper/>.

- Start the `hyprpaper` daemon:

`hyprpaper`

- Change the wallpaper for a specific monitor:

`hyprctl hyprpaper wallpaper "{{monitor}},{{path/to/image.png}}"`

- Change the default wallpaper for all unspecified monitors and set its fit mode:

`hyprctl hyprpaper wallpaper ",{{path/to/image.png}},{{contain|cover|tile|fill}}"`
