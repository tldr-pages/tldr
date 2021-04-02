# spectre-meltdown-checker

> Spectre and Meltdown mitigation detection tool.
> More information: <https://manned.org/spectre-meltdown-checker.1>.

- Check the currently running kernel for Spectre and Meltdown:

`spectre-meltdown-checker`

- Check the currently running kernel and show an explanation of the actions to take in order to mitigate a vulnerability:

`spectre-meltdown-checker --explain`

- Check for specific variants (defaults to all):

`spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- Don't use the `/sys` interface even if present:

`spectre-meltdown-checker --no-sysfs`

- Check a non-running kernel:

`spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
