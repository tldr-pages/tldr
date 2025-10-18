# intercept

> Read raw input events from a specified input event device and redirect it to `stdout`.
> More information: <https://gitlab.com/interception/linux/tools/-/tree/master#intercept>.

- Read and output raw input events from a given input device file (the system will not see any key presses):

`sudo intercept -g {{/dev/input/eventX}}`

- Read and output raw input events from a given input device file (the system can see key presses and does not block other programs from reading them):

`sudo intercept {{/dev/input/eventX}}`
