# cfv

> Command-line File Verify, a utility to test and create checksum files.
> More information: <https://manned.org/cfv>.

- [T]est checksum files in current directory:

`cfv -T`

- [T]est [v]erbosely, re[n]ame bad, and show [u]nverified files using a checksum [f]ile:

`cfv -Tvnu -f {{path/to/file}}`

- [C]reate a checksum file of a secific [t]ype for the selected files:

`cfv -C -t "{{sfv|sha256|md5|...}}" {{file1 file2 ...}}`

- [C]reate separate checksum files for each [r]ecursively selected directory:

`cfv -Cr`

- [C]reate a single `sha256` type [f]ile for all [rr]ecursively selected files:

`cfv -C -f {{sums.sha256}} -rr`

- [C]reate a `g[z]ipped` `.sfv` file [v]erbosely, following `sym[l]inks` and using `path/to/directory` as base [p]ath:

`cfv -Czvl -p {{path/to/directory}}`
