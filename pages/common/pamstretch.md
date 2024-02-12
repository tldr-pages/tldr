# pamstretch

> Scale up a PAM image by interpolating between pixels.
> See also: `pamstretch-gen`, `pamenlarge`, `pamscale`.
> More information: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Scale up a PAM image by an integer factor:

`pamstretch {{N}} {{path/to/image.pam}} > {{path/to/output.pam}}`

- Scale up a PAM image by the specified factors in the horizontal and vertical directions:

`pamstretch -xscale {{XN}} -yscale {{YN}} {{path/to/image.pam}} > {{path/to/output.pam}}`
