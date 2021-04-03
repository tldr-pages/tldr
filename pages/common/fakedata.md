# fakedata

> Generate fake data using a large variety of generators.
> More information: <https://github.com/lucapette/fakedata>.

- List all valid generators:

`fakedata --generators`

- Generate data using one or more generators:

`fakedata {{generator1}} {{generator2}}`

- Generate data with a specific output format:

`fakedata --format {{csv|tab|sql}} {{generator}}`

- Generate {{n}} data:

`fakedata --limit {{n}} {{generator}}`

- Generate data using a custom output template (capitalize the first letter of generators):

`echo "value: {{Generator}}" | fakedata`
