# pt

> Platinum Searcher.
> A code search tool similar to `ag`.
> More information: <https://github.com/monochromegane/the_platinum_searcher>.

- Find files containing a pattern and print the files with highlighted matches:

`pt {{pattern}}`

- Find files containing a pattern and display count of matches in each file:

`pt {{[-c|--count]}} {{pattern}}`

- Find files containing a pattern as a whole word and ignore its case:

`pt {{[-wi|--word-regexp --ignore-case]}} {{pattern}}`

- Find a pattern in files with a given extension using a `regex`:

`pt {{[-G|--file-search-regexp]}}='{{\.ext$}}' {{pattern}}`

- Find files whose contents match the `regex`, up to 2 directories deep:

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`
