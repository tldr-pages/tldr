# swaybg

> Wallpaper tool for Wayland compositors.
> Note: Sway starts `swaybg` automatically if a wallpaper is set in the config file.
> More information: <https://github.com/swaywm/swaybg/blob/master/swaybg.1.scd>.

- Set the wallpaper on all monitors to an image:

`swaybg {{[-i|--image]}} {{path/to/image}}`

- Set the image scaling mode (default: `stretch`):

`swaybg {{[-i|--image]}} {{path/to/image}} {{[-m|--mode]}} {{stretch|fit|fill|center|tile|solid_color}}`

- Set the wallpaper to a static color:

`swaybg {{[-c|--color]}} {{rrggbb}}`

- Set the wallpaper on a specific monitor:

`swaybg {{[-o|--output]}} {{HDMI-1}} {{[-i|--image]}} {{path/to/image}}`

- Set different wallpapers on multiple monitors:

`swaybg {{[-o|--output]}} {{HDMI-1}} {{[-i|--image]}} {{path/to/image}} {{[-o|--output]}} {{DP-1}} {{[-i|--image]}} {{path/to/image}}`
