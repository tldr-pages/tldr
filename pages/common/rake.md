# rake

> A Make-like program for Ruby.
> Tasks for `rake` are specified in a Rakefile.
> More information: <https://ruby.github.io/rake>.

- Run the `default` Rakefile task:

`rake`

- Run a specific task:

`rake {{task}}`

- Execute `n` jobs at a time in parallel (number of CPU cores + 4 by default):

`rake --jobs {{n}}`

- Use a specific Rakefile:

`rake --rakefile {{path/to/Rakefile}}`

- Execute `rake` from another directory:

`rake --directory {{path/to/directory}}`
