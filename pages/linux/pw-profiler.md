# pw-profiler

> Profile a local or remote instance.
> More information: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- Profile the default instance, logging to `profile.log` (`gnuplot` files and a HTML file for result visualizing are also generated):

`pw-profiler`

- Change the log output file:

`pw-profiler --output {{path/to/file.log}}`

- Profile a remote instance:

`pw-profiler --remote {{remote_name}}`

- Display help:

`pw-profiler --help`
