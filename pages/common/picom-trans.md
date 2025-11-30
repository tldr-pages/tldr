# picom-trans

> Set the window opacity for the `picom` window compositor.
> More information: <https://github.com/yshui/picom/blob/next/man/picom-trans.1.adoc>.

- Set the currently focused window opacity to a specific percentage:

`picom-trans {{[-c|--current]}} {{[-o|--opacity]}} {{percentage}}`

- Set the opacity of a window with a specific name:

`picom-trans {{[-n|--name]}} {{Firefox}} {{[-o|--opacity]}} {{percentage}}`

- Set the opacity of a specific window selected via mouse cursor:

`picom-trans {{[-s|--select]}} {{[-o|--opacity]}} {{90}}`

- Toggle the opacity of a specific window:

`picom-trans {{[-n|--name]}} {{Firefox}} {{[-t|--toggle]}}`
