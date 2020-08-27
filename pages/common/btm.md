# btm

> An alternative to `top`.
> Aims to be lightweight, cross-platform and more graphical than `top`.
> More information: <https://github.com/ClementTsang/bottom>.

- Show default layout (cpu + memory + temperatures + disk + network + processes):

`btm`

- Enable basic mode, removing charts and condensing data (similar to "top"):

`btm --basic`

- Use big dots instead of small ones in charts:

`btm --dot-marker`

- Show also battery charge and health status:

`btm --battery`

- Refresh every 250 milliseconds and show last 30 seconds in charts:

`btm --rate 250 --default_time_value 30000`
