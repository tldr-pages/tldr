# gource

> Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories.
> It shows files and directories being created, modified or removed over time.
> More information: <https://gource.io>.

- Run gource in a directory (if it isn't the repository's root directory, the root is sought up from there):

`gource {{path/to/repository}}`

- Run gource in the current directory, with a custom output resolution:

`gource -{{width}}x{{height}}`

- Specify the timescale for the animation:

`gource -c {{time_scale_multiplier}}`

- Specify how long each day should be in the animation (this combines with -c, if provided):

`gource -s {{seconds}}`

- Use fullscreen mode and a custom background color:

`gource -f -b {{hex_color_code}}`

- Specify the animation title:

`gource --title {{title}}`
