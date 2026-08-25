# sg_raw

> Send arbitrary SCSI command to a connected device.
> More information: <https://manned.org/sg_raw>.

- Send a command to an optical SCSI device assigned to `sr0` to load the media in its tray:

`sg_raw /dev/sr0 EA 00 00 00 00 01`

- Read data from `IFILE` instead of `stdin`:

`sg_raw {{[-i|--infile]}} {{path/to/IFILE}} {{/dev/sgX}} {{scsi_command}}`

- Skip the first `LEN` bytes of input data:

`sg_raw {{[-k|--skip]}} {{LEN}} {{/dev/sgX}} {{scsi_command}}`

- Read `SLEN` bytes of data and send to the device:

`sg_raw {{[-s|--send]}} {{SLEN}} {{/dev/sgX}} {{scsi_command}}`

- Wait up to `SEC` seconds for `sg_raw` to finish processing:

`sg_raw {{[-t|--timeout]}} {{SEC}} {{/dev/sgX}} {{scsi_command}}`

- Increase verbosity level by 1:

`sg_raw {{[-v|--verbose]}} {{/dev/sgX}} {{scsi_command}}`

- Dump returned data in binary form:

`sg_raw {{[-b|--binary]}} {{/dev/sgX}} {{scsi_command}}`

- Write data received from the specified device to an `OFILE`:

`sg_raw {{[-o|--outfile]}} {{path/to/OFILE}} {{/dev/sgX}} {{scsi_command}}`
