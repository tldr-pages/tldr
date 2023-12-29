# pamscale

> Scale a Netpbm image.
> More information: <https://netpbm.sourceforge.net/doc/pamscale.html>.

- Scale an image such that the result has the specified dimensions:

`pamscale -width {{width}} -height {{height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Scale an image such that the result has the specified width, keeping the aspect ratio:

`pamscale -width {{width}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Scale an image such that its width and height is changed by the specified factors:

`pamscale -xscale {{x_factor}} -yscale {{y_factor}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Scale an image such that it fits into the specified bounding box while preserving its aspect ratio:

`pamscale -xyfit {{bbox_width}} {{bbox_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Scale an image such that it completely fills the specified box while preserving its aspect ratio:

`pamscale -xyfill {{box_width}} {{box_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`
