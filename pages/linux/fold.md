# Fold

> Folds long lines for fixed-width output devices.
> More information: <https://www.ibm.com/docs/en/aix/7.1?topic=f-fold-command>.

- Fold lines in a fixed widht:

`fold -w {{widht}} {{file_name}}`

- Counts Width in bytes (the default is to count in columns).

`fold -b -w {{widht_in_bytes}} {{file_name}}`

- Breaks the line after the rightmost blank within the Width limit:

`fold -s -w {{widht}} {{file_name}}`
