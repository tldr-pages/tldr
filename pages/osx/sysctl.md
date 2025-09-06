# sysctl

> Access kernel state information.
> More information: <https://keith.github.io/xcode-man-pages/sysctl.8.html>.

- Show all available variables and their values:

`sysctl -a`

- Show Apple model identifier:

`sysctl -n hw.model`

- Show CPU model:

`sysctl -n machdep.cpu.brand_string`

- Show available CPU features (MMX, SSE, SSE2, SSE3, AES, etc):

`sysctl -n machdep.cpu.features`

- Set a changeable kernel state variable:

`sysctl -w {{section.tunable}}={{value}}`
