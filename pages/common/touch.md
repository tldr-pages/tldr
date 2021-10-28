# touch

> Change a file access and modification times (atime, mtime).
> More information: <https://www.gnu.org/software/coreutils/touch>.

- Create a new empty file(s) or change the times for existing file(s) to current time:

`touch {{path/to/file}}`

- Set the times on a file to a specific date and time:

`touch -t {{YYYYMMDDHHMM.SS}} {{path/to/file}}`

- Set the time on a file to one hour in the past:

`touch -d "{{-1 hour}}" {{path/to/file}}`

- Use the times from a file to set the times on a second file:

`touch -r {{filename}} {{path/to/file}}`

- Create multiple files:

`touch {{file{1,2,3}.txt}}`
