# exa
> Modern replacement for the venerable file-listing command-line program `ls` that ships with Unix and Linux operating systems, giving it more features and better defaults. It uses colours to distinguish file types and metadata.
> More information: <https://github.com/ogham/exa>.

- List all files in grid:

`exa`

- List files in grid but sort the grid across, rather than downwards:

`exa -x`

- Display extended details and attributes of files:

`exa -l`

- Display extended details of all files in directory (including hidden ones):

`exa -la`

- List directories before other files:

`exa -la --group-directories-first`