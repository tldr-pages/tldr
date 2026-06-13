# pt

> Platinum Searcher.
> A code search tool similar to `ag`.
> More information: <https://github.com/monochromegane/the_platinum_searcher>.

- Find files containing "foo" and print the files with highlighted matches:

`pt {{foo}}`

- Find files containing "foo" and display count of matches in each file:

`pt {{[-c|--count]}} {{foo}}`

- Find files containing "foo" as a whole word and ignore its case:

`pt {{[-wi|--word-regexp --ignore-case]}} {{foo}}`

- Find "foo" in files with a given extension using a `regex`:

`pt {{[-G|--file-search-regexp]}}='{{\.bar$}}' {{foo}}`

- Find files whose contents match the `regex`, up to 2 directories deep:

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`
