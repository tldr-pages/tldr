# fold

> Folds long lines for fixed-width output devices.
> Meer informatie: <https://www.gnu.org/software/coreutils/fold>.

- Fold lines in a fixed width:

`fold --width {{breedte}} {{pad/naar/bestand}}`

- Count width in bytes (the default is to count in columns):

`fold --bytes --width {{breedte_in_bytes}} {{pad/naar/bestand}}`

- Break the line after the rightmost blank within the width limit:

`fold --spaces --width {{breedte}} {{pad/naar/bestand}}`
