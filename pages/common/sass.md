# Sass

> Converts SCSS or Sass files to CSS.

- Output converted file to stdout:

`sass {{inputfile.scss|inputfile.sass}}`

- Immediately convert SCSS or Sass file to CSS to specified output file:

`sass {{inputfile.scss|inputfile.sass}} {{outputfile.css}}`

- Watch SCSS or Sass file for changes and output or update CSS file with same filename:

`sass --watch {{inputfile.scss|inputfile.sass}}`

- Watch SCSS or Sass file for changes and output or update CSS file with specified filename:

`sass --watch {{inputfile.scss|inputfile.sass}}:{{outputfile.css}}`
