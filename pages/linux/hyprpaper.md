# hyprpaper

> Wallpaper utility for Hyprland with the ability to dynamically change wallpapers.
> Controlled by the config file `~/.config/hypr/hyprpaper.conf`.
> More information: <https://github.com/hyprwm/hyprpaper>.

- Start the hyprpaper service:

`hyprpaper`

- Preload a wallpaper:

`hyprctl hyprpaper preload "{{path/to/image.png}}"`

- Switch wallpaper to a different preloaded image:

`hyprctl hyprpaper wallpaper "{{monitor}},{{path/to/image.png}}"`

- Preload a wallpaper, set that wallpaper, then unload all unused wallpapers:

`hyprctl hyprpaper reload "{{monitor}},{{path/to/image.png}}"`

- List the wallpapers that are currently preloaded (useful for dynamically preloading and unloading):

`hyprctl hyprpaper listloaded`

- List the active wallpapers hyprpaper is displaying, along with their associated monitor:

`hyprctl hyprpaper listactive`
