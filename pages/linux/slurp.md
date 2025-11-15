# slurp

> Select a region in a Wayland compositor.
> More information: <https://github.com/emersion/slurp/blob/master/slurp.1.scd>.

- Select a region and print it to `stdout`:

`slurp`

- Select a region and print it to `stdout`, while displaying the dimensions of the selection:

`slurp -d`

- Select a single point instead of a region:

`slurp -p`

- Select an output and print its name:

`slurp -o -f '%o'`

- Select a specific region and take a borderless screenshot of it, using `grim`:

`grim -g "$(slurp -w 0)"`

- Select a specific region and take a borderless video of it, using `wf-recorder`:

`wf-recorder {{[-g|--geometry]}} "$(slurp -w 0)"`
