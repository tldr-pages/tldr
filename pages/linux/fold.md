# Fold

> Folds long lines for fixed-width output devices.
> More information: <https://www.ibm.com/docs/en/aix/7.1?topic=f-fold-command>.

- Fold lines in a fixed width:

`fold -w {{width}} {{file_name}}`

- Count Width in bytes (the default is to count in columns):

`fold -b -w {{width_in_bytes}} {{file_name}}`

- Break the line after the rightmost blank within the Width limit:

`fold -s -w {{width}} {{file_name}}`
