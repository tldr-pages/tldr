# mods

> AI for the command line, built for pipelines.
> More information: <https://github.com/charmbracelet/mods>.

- Ask a generic question:

`mods "{{write me a poem about platypuses}}"`

- Open settings in your `$EDITOR`:

`mods --settings`

- Ask for comments on your code, in a markdown [f]ormat:

`mods -f "{{what are your thoughts on improving this code?}}" < {{path/to/file}}`

- Ask for help with your documentation, in a markdown [f]ormat:

`mods -f "{{write a new section to this readme for a feature that sends you a free rabbit if you hit r}}"`

- Organize your videos, in a markdown [f]ormat:

`ls {{path/to/videos}} | mods -f "{{organize these by decade and summarize}}"`

- Read through raw HTML and summarize the contents, in a markdown [f]ormat:

`curl "{{https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m" 2>/dev/null}} | mods -f "{{summarize this weather data for a human.}}"`

- Display [h]elp and exit:

`mods -h`
