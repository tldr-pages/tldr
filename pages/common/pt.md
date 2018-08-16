# pt

> Platinum Searcher. A code search tool similar to ag. Respects .gitignore.

- Find files containing "foo" and print the files with highlighted matches:

`pt foo`

- Find files containing "foo" and display count of matches in each file:

`pt -c foo`

- Find files containing "foo" as a whole word and ignore its case:

`pt -wi foo`

- Find "foo" in files with a name matching provided regular expression:

`pt -G='\.bar' foo`

- Find files whose contents match the regular expression, up to 2 folders deep:

`pt --depth=2 -e '[^ba[rz]*$]'`
