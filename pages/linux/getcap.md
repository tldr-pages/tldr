# getcap

> Command to display the name and capabilities of each specified file.
> More information: <https://www.man7.org/linux/man-pages/man8/getcap.8.html>.

- Get capabilities for the given files:

`getcap {{path/to/file1 path/to/file2 ...}}`

- Displays all searched entries even if no capabilities are set:

`getcap -v {{path/to/file1 path/to/file2 ...}}`
