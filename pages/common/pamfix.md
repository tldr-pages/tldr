# pamfix

> Fix errors in PAM, PBM, PGM and PPM files.
> See also: `pamfile`, `pamvalidate`.
> More information: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Fix a Netpbm file that is missing its last part:

`pamfix -truncate {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- Fix a Netpbm file where pixel values exceed the image's `maxval` by lowering the offending pixels' values:

`pamfix -clip {{path/to/corrupted.ext}} > {{path/to/output.ext}}`

- Fix a Netpbm file where pixel values exceed the image's `maxval` by increasing it:

`pamfix -changemaxval {{path/to/corrupted.pam|pbm|pgm|ppm}} > {{path/to/output.pam|pbm|pgm|ppm}}`
