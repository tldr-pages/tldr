# sass

> Convert SCSS or Sass files to CSS.
> More information: <https://sass-lang.com/documentation/cli/dart-sass>.

- Convert a SCSS or Sass file to CSS and print out the result:

`sass {{inputfile.scss|inputfile.sass}}`

- Convert a SCSS or Sass file to CSS and save the result to a file:

`sass {{inputfile.scss|inputfile.sass}} {{outputfile.css}}`

- Watch a SCSS or Sass file for changes and output or update the CSS file with same filename:

`sass --watch {{inputfile.scss|inputfile.sass}}`

- Watch a SCSS or Sass file for changes and output or update the CSS file with the given filename:

`sass --watch {{inputfile.scss|inputfile.sass}}:{{outputfile.css}}`
