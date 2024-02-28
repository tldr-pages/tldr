# pamfix

> Fix errors in Netpbm files.
> See also: `pamfile`, `pamvalidate`.
> More information: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Fix a Netpbm file that is missing its last part:

`pamfix -truncate {{path/to/corrupted.pam}} > {{path/to/output.pam}}`

- Fix a Netpbm file where pixel values exceed the image's maxval by lowering the offending pixels' values:

`pamfix -clip {{path/to/corrupted.pam}} > {{path/to/output.pam}}`

- Fix a Netpbm file where pixel values exceed the image's maxval increasing the maxval:

`pamfix -changemaxval {{path/to/corrupted.pam}} > {{path/to/output.pam}}`
