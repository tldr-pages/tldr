# swaplabel

> Print or change the label or UUID of a swap area.
> Note: `path/to/file` can either point to a regular file or a swap partition.
> More information: <https://man7.org/linux/man-pages/man8/swaplabel.8.html>.

- Set a swap partition label:

`swaplabel --label "{{new_label}}" /dev/{{sda1}}"`
