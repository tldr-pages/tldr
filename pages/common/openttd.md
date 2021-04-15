# openttd

> Open source clone of the Microprose game "Transport Tycoon Deluxe".
> More information: <https://www.openttd.org>.

- Load new/save game at start:

`openttd -g {{path/to/file}}`

- Start with a set resolution (eg. 1920x1200):

`openttd -r {{resolution}}`

- Start with a custom configuration file:

`openttd -c {{path/to/file}}`

- Start with selected drivers:

`openttd -v {{video_driver}} -s {{sound_driver}} -m {{music_driver}}`

- Start a dedicated server, forked in the background:

`openttd -f -D {{host}}:{{port}}`

- Join a server with a password:

`openttd -n {{host}}:{{port}}#{{player_name}} -p {{password}}`
