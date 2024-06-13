# azurite

> Azure Storage API compatible server (emulator) in local environment.
> More information: <https://www.npmjs.com/package/azurite>.

- Use an existing location as workspace path:

`azurite {{-l|--location}} {{path/to/directory}}`

- Disable access log displayed in console:

`azurite {{-s|--silent}}`

- Enable debug log by providing a file path as log destination:

`azurite {{-d|--debug}} {{path/to/debug.log}}`

- Customize the listening address of Blob/Queue/Table service:

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- Customize the listening port of Blob/Queue/Table service:

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`
