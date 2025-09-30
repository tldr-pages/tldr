# pamoil

> Turn a PAM image into an oil painting.
> More information: <https://netpbm.sourceforge.net/doc/pamoil.html>.

- Turn a PAM image into an oil painting:

`pamoil {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`

- Consider a neighborhood of `n` pixels for the "smearing" effect:

`pamoil -n {{n}} {{path/to/input_file.pam}} > {{path/to/output_file.pam}}`
