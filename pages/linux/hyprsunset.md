# hyprsunset

> A blue light filter for Hyprland.
> Controlled by the config file ~/.config/hypr/hyprsunset.conf.
> This file is not required for running hyprsunset, but is recommended.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprsunset/>.

- Start the hyprsunset service:
`hyprsunset`

- Start the hyprsunset service with a specified color temperature and gamma percentage:
`hyprsunset {{[-t|--temperature]}} {{temperature}} {{[-g|--gamma]}} {{gamma}}`

- Adjust color temperature while the hyprsunset service is running:
`hyprctl hyprsunset temperature {{temperature}}`

- Adjust gamma while the hyprsunset service is running:
`hyprctl hyprsunset gamma {{gamma}}`

- Reset color temperature to 6000k:
`hyprctl hyprsunset reset temperature`

- Reset gamma to 100%:
`hyprctl hyprsunset reset gamma`
