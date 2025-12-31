# ruby

> Ruby programming language interpreter.
> See also: `gem`, `bundler`, `rake`, `irb`.
> More information: <https://manned.org/ruby>.

- Execute a Ruby script:

`ruby {{path/to/script.rb}}`

- Execute a single Ruby command in the command-line:

`ruby -e "{{command}}"`

- Check for syntax errors on a given Ruby script:

`ruby -c {{path/to/script.rb}}`

- Start the built-in HTTP server on port 8080 in the current directory:

`ruby -run -e httpd`

- Locally execute a Ruby binary without installing the required library it depends on:

`ruby -I {{path/to/library_folder}} -r {{library_require_name}} {{path/to/bin_folder/bin_name}}`

- Display version:

`ruby {{[-v|--version]}}`
