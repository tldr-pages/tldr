# fakedata

> CLI utility for fake data generation.
> More information: <https://github.com/lucapette/fakedata>.

- List generators (all kinds of data that can be generated):

`fakedata --generators`

- Generate data for one or several generators:

`fakedata {{generator1}} {{generator2}}`

- Generate data with a specific format:

`fakedata --format {{csv|tab|sql}} {{generator}}`

- Generate {{n}} data:

`fakedata --limit {{n}} {{generator}}`

- Generate data using a custom template (capitalize the first letter of generators):

`echo "value: {{Generator}}" | fakedata`
