# bundle

> Dependency manager for the Ruby programming language.
> More information: <https://bundler.io/man/bundle.1.html>.

- Install all gems defined in the `Gemfile` expected in the working directory:

`bundle install`

- Execute a command in the context of the current bundle:

`bundle exec {{command}} {{arguments}}`

- Update all gems by the rules defined in the `Gemfile` and regenerate `Gemfile.lock`:

`bundle update`

- Update one or more specific gem(s) defined in the `Gemfile`:

`bundle update {{gemname}} {{gemname}}`

- Update one or more specific gems(s) defined in the `Gemfile` but only to the next patch version:

`bundle update --patch {{gemname}} {{gemname}}`

- Update update all gems within the given group in the `Gemfile`:

`bundle update --group {{development}}`

- List installed gems in the `Gemfile` with newer versions available:

`bundle outdated`

- Create a new gem skeleton:

`bundle gem {{gemname}}`
