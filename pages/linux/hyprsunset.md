# hyprsunset

> A blue light filter for Hyprland.
> Optionally configured via `~/.config/hypr/hyprsunset.conf`.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprsunset/>.

- Start the hyprsunset service:

`hyprsunset`

- Start the hyprsunset service with a specified color temperature and gamma percentage:

`hyprsunset {{[-t|--temperature]}} {{temperature}} {{[-g|--gamma]}} {{gamma}}`

- Adjust the color temperature while the hyprsunset service is running:

`hyprctl hyprsunset temperature {{temperature}}`

- Adjust the gamma while the hyprsunset service is running:

`hyprctl hyprsunset gamma {{gamma}}`

- Reset the color temperature to 6000K:

`hyprctl hyprsunset reset temperature`

- Reset the gamma to 100%:

`hyprctl hyprsunset reset gamma`
