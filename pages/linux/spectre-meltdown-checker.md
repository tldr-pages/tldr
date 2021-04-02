# spectre-meltdown-checker

> Spectre and Meltdown mitigation detection tool.
> More information: <https://manned.org/spectre-meltdown-checker.1>.

- Check the currently running kernel for Spectre and Meltdown:

`spectre-meltdown-checker`

- Check the currently running kernel and show explanations for taken actions to mitigate a vulnerability:

`spectre-meltdown-checker --explain`

- Don't use the `/sys` interface even if present:

`spectre-meltdown-checker --no-sysfs`

- Check for specific variants (`1`, `2`, `3`, `3a`, `4`, `l1tf`, `msbds`, `mfbds`, `mlpds`, `mdsum`, `taa`, `mcespc`, `srbds` - defaults to all):

`spectre-meltdown-checker --variant {{3a}} --variant {{mcespc}}`

- Inspect a non-running kernel:

`spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
