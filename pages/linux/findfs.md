# findfs

> Finds a filesystem by label or UUID.
> More information: <https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>.

- Search block devices by filesystem label:

`findfs LABEL={{label}}`

- Search block devices by filesystem UUID:

`findfs UUID={{label}}`

- Search block devices by partition UUID (GPT or MAC partition table):

`findfs PARTLABEL={{label}}`

- Search block devices by partition label (GPT partition table only):

`findfs PARTUUID={{label}}`
