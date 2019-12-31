# bundle

> Dependency manager for the Ruby programming language.
> More information: <https://bundler.io/man/bundle.1.html>.

- Install all gems defined in the `Gemfile` expected in the working directory:

`bundle install`

- Update all gems by the rules defined in the `Gemfile` and regenerate `Gemfile.lock`:

`bundle update`

- Update one specific gem defined in the `Gemfile`:

`bundle update --source {{gemname}}`

- Create a new gem skeleton:

`bundle gem {{gemname}}`
