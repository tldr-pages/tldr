# pamslice

> Extract one line of values out of a PAM image.
> More information: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Print the values of the pixels in the n'th row in a table:

`pamslice {{[-r|-row]}} {{n}} {{path/to/image.pam}}`

- Print the values of the pixels in the n'th column in a table:

`pamslice {{[-c|-column]}} {{n}} {{path/to/image.pam}}`

- Consider the m'th plane of the input image only:

`pamslice {{[-r|-row]}} {{n}} -plane {{m}} {{path/to/image.pam}}`

- Produce output in a format suitable for input to an `xmgr` for visualisation:

`pamslice {{[-r|-row]}} {{n}} {{[-x|-xmgr]}} {{path/to/image.pam}}`
