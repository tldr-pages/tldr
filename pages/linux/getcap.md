# getcap

> Command to display the name and capabilities of each specified file.
> More information: <https://manned.org/getcap>.

- Get capabilities for the given files:

`getcap {{path/to/file1 path/to/file2 ...}}`

- Get capabilities for all the files recursively under the given directories:

`getcap -r {{path/to/directory1 path/to/directory2 ...}}`

- Displays all searched entries even if no capabilities are set:

`getcap -v {{path/to/file1 path/to/file2 ...}}`
