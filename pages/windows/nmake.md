# nmake

> The Microsoft Program Maintenance Utility for building projects based on commands in a makefile.
> More information: <https://learn.microsoft.com/cpp/build/reference/nmake-reference>.

- Build targets using the default makefile in the current directory:

`nmake`

- Build targets using a specific makefile:

`nmake /F {{path/to/makefile}}`

- Build a specific target:

`nmake {{target}}`

- Display commands without executing them:

`nmake /N`

- Display all macro definitions and target descriptions:

`nmake /P`

- Continue building unrelated targets on error:

`nmake /K`

- Build and ignore timestamp checks (force rebuild):

`nmake /A`

- Suppress copyright message:

`nmake /NOLOGO`
