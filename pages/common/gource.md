# gource

> Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories.
> It shows files and folders being created, modified or removed over time.

- Run gource in a directory:

`gource {{/path/to/repository/}}`

- Run gource in fullscreen mode (assuming the command is run from the project's root directory):

`gource -f`

- Set the resolution:

`gource -{{width}}x{{height}}`

- Set the animation time scale:

`gource -c {{time_scale_multiplier}}`

- Set the amount of time to display each day:

`gource -s {{seconds}}`

- Set the background color:

`gource -b {{hex_color_code}}`

- Set the title:

`gource --title {{title}}`
