# wwt

> Wiimms WBFS Tool for managing WBFS files and partitions.
> More information: <https://wit.wiimm.de/wwt/>.

- List all discs in a WBFS file:

`wwt LIST --part {{path/to/file.wbfs}}`

- Add ISO images to a WBFS file:

`wwt ADD --part {{path/to/file.wbfs}} {{path/to/image.iso}}`

- Extract a disc from a WBFS file by its ID6:

`wwt EXTRACT --part {{path/to/file.wbfs}} {{id6}}`

- Remove a disc from a WBFS file by its ID6:

`wwt REMOVE --part {{path/to/file.wbfs}} {{id6}}`

- Check a WBFS file for allocation errors:

`wwt CHECK {{path/to/file.wbfs}}`

- Repair errors in a WBFS file:

`wwt REPAIR {{path/to/file.wbfs}}`

- Verify all discs in a WBFS file using SHA1 checksums:

`wwt VERIFY --part {{path/to/file.wbfs}}`
