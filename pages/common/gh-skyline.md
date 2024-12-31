# gh skyline

> Generate a 3D model of your GitHub contribution history.
> By default, it will create a `{username}-{year}-github-skyline.stl` file in the current directory.
> More information: <https://github.com/github/gh-skyline>.

- Generate a skyline STL file for the current year and authenticated user:

`gh skyline`

- Generate a skyline for a specific [u]ser and [y]ear:

`gh skyline --user {{username}} --year {{year}}`

- Generate a skyline for a range of [y]ears:

`gh skyline --user {{username}} --year {{first_year}}-{{last_year}}`

- Generate a [f]ull skyline (from the user's join year to the current year):

`gh skyline --user {{username}} --full`

- Enable [d]ebug logging:

`gh skyline --debug`

- Generate a skyline and specify the [o]utput file path:

`gh skyline --output {{path/to/output_file.stl}}`

- Open the GitHub profile for a specific [u]ser:

`gh skyline --user {{username}} --web`

- Display [h]elp:

`gh skyline --help`
