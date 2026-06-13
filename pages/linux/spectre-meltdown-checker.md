# spectre-meltdown-checker

> Spectre and Meltdown mitigation detection tool.
> More information: <https://manned.org/spectre-meltdown-checker>.

- Check the currently running kernel for Spectre or Meltdown:

`sudo spectre-meltdown-checker`

- Check the currently running kernel and show an explanation of the actions to take to mitigate a vulnerability:

`sudo spectre-meltdown-checker --explain`

- Check for specific variants (defaults to all):

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- Display output using a specific output format:

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- Don't use the `/sys` interface even if present:

`sudo spectre-meltdown-checker --no-sysfs`

- Check a non-running kernel:

`sudo spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
