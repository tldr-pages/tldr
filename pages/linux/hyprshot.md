# hyprshot

> Screenshot utility for the Hyprland Wayland compositor.
> More information: <https://github.com/Gustash/Hyprshot>.

- Select and take a screenshot of a region:

`hyprshot {{[-m|--mode]}} region`

- Select and take a screenshot of a specific window:

`hyprshot {{[-m|--mode]}} window`

- Select and take a screenshot of a specific output:

`hyprshot {{[-m|--mode]}} output`

- Take a screenshot of the currently active window:

`hyprshot {{[-m|--mode]}} active {{[-m|--mode]}} window`

- Freeze the screen and take a screenshot of the selected region:

`hyprshot {{[-z|--freeze]}} {{[-m|--mode]}} region`

- Select and take a screenshot of a specific window, saving to the given output directory:

`hyprshot {{[-o|--output-folder]}} {{path/to/directory}} {{[-m|--mode]}} window`

- Select and take a screenshot of a specific output, saving the screenshot to the clipboard only:

`hyprshot --clipboard {{[-m|--mode]}} output`
