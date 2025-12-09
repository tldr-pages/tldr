# gh skyline

> Generate a 3D model of your GitHub contribution history.
> By default, it will create a `{username}-{year}-github-skyline.stl` file in the current directory.
> More information: <https://github.com/github/gh-skyline>.

- Generate a skyline STL file for the current year and authenticated user:

`gh skyline`

- Generate a skyline for a specific user and year:

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{year}}`

- Generate a skyline for a range of years:

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{first_year}}-{{last_year}}`

- Generate a full skyline (from the user's join year to the current year):

`gh skyline {{[-u|--user]}} {{username}} {{[-f|--full]}}`

- Enable debug logging:

`gh skyline {{[-d|--debug]}}`

- Generate a skyline and specify the output file path:

`gh skyline {{[-o|--output]}} {{path/to/output_file.stl}}`

- Open the GitHub profile for a specific user:

`gh skyline {{[-u|--user]}} {{username}} {{[-w|--web]}}`

- Display help:

`gh skyline {{[-h|--help]}}`
