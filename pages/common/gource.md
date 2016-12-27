# gource

> Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories.
> It shows files and folders being created, modified or removed over time.

- Run gource in a directory (if it isn't the repository's root directory, the root is seeked up from there):

`gource {{path/to/repository}}`

- Set the resolution:

`gource -{{width}}x{{height}}`

- Set the animation time scale:

`gource -c {{time_scale_multiplier}}`

- Set the amount of time to display each day:

`gource -s {{seconds}}`

- Run gource in fullscreen mode and set the background color:

`gource -f -b {{hex_color_code}}`

- Set the title:

`gource --title {{title}}`
