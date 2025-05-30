# intercept

> A tool that reads raw input events from a specified input event device and redirects it to stdout.
> More information: <https://gitlab.com/interception/linux/tools/-/tree/master?ref_type=heads#intercept>.

- Read and output raw input events from a given input device file (system won’t see key presses):

## `sudo intercept -g {{/dev/input?eventX}}`

- Read and output raw input events from a given input device file (system can see key presses and doesn't block other programs from reading them):

`sudo intercept {{/dev/input/eventX}}`
