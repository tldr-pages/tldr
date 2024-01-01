# cupstestppd

> Test conformance of PPD files to the version 4.3 of the specification.
> Error codes (1, 2, 3 and 4, respectively): bad CLI arguments, unable to open file, unskippable format errors and non-conformance with PPD specification.
> NOTE: this command is deprecated.
> See also: `lpadmin`.
> More information: <https://openprinting.github.io/cups/doc/man-cupstestppd.html>.

- Test the conformance of one or more files in quiet mode:

`cupstestppd -q {{path/to/file1.ppd path/to/file2.ppd ...}}`

- Get the PPD file from `stdin`, showing detailed conformance testing results:

`cupstestppd -v - < {{path/to/file.ppd}}`

- Test all PPD files under the current directory, printing the names of each file that does not conform:

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`
