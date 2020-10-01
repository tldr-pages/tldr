# csvtool

> Utility to filter and extract data from CSV formatted sources.
> More information: <https://github.com/maroofi/csvtool/>.

- Extract 2nd column from example.csv:

`csvtool -c 2 test.csv`

- Extract 2nd and 4th column from example.csv:

`csvtool -c 2,4 test.csv`

- Extract lines where 2nd column exactly matches 'Foo':

`csvtool -c 2 -s '^Foo$' test.csv`

- Extract lines where 2nd column starts with 'Bar':

`csvtool -c 2 -s '^Bar' test.csv`

- Find lines where 2nd column ends with 'Baz' and extract the 3rd and 6th columns:

`csvtool -c 2 -s 'Baz$' test.csv | csvtool --no-header -c 3,6`
