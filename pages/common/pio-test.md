# pio test

> Run local tests on a PlatformIO project.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Run all tests in all environments of the current PlatformIO project:

`pio test`

- Test only specific environments:

`pio test {{[-e|--environment]}} {{environment1}} {{[-e|--environment]}} {{environment2}}`

- Run only tests whose name matches a specific glob pattern:

`pio test {{[-f|--filter]}} "{{pattern}}"`

- Ignore tests whose name matches a specific glob pattern:

`pio test {{[-i|--ignore]}} "{{pattern}}"`

- Specify a port for firmware uploading:

`pio test --upload-port {{upload_port}}`

- Specify a custom configuration file for running the tests:

`pio test {{[-c|--project-conf]}} {{path/to/platformio.ini}}`
