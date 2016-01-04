# Sass

> Converts SCSS or Sass files to CSS
> .scss and .sass can be used interchangeably in below examples depending on your preference

- Immediately convert scss file and output css with same filename

`sass {{inputfile}}.scss`

- Immediately convert SCSS or Sass file to CSS to specified output file

`sass {{inputfile}}.scss {{outputfile}}.css`

- Watch SCSS or Sass file for changes and output or update CSS file with same filename

`sass --watch {{inputfile}}.scss`

- Watch SCSS or Sass file for changes and output or update CSS file with specified filename

`sass --watch {{inputfile}}.scss:{{outputfile}}.css`