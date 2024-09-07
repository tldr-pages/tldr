# tunelp

> Set various parameters for parallel port devices for troubleshooting or for better performance.
> Part of `util-linux`.
> More information: <https://manned.org/tunelp>.

- Check the [s]tatus of a parallel port device:

`tunelp --status {{/dev/lp0}}`

- [r]eset a given parallel port:

`tunelp --reset {{/dev/lp0}}`

- Use a given [i]RQ for a device, each one representing an interrupt line:

`tunelp -i 5 {{/dev/lp0}}`

- Try a given number of times to output a [c]haracter to the printer before sleeping for a given [t]ime:

`tunelp --chars {{times}} --time {{time_in_centiseconds}} {{/dev/lp0}}`

- Enable or disable [a]borting on error (disabled by default):

`tunelp --abort {{on|off}}`
