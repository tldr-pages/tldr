# chat

> Automate conversations with a modem or serial device.
> Commonly used to establish PPP (Point-to-Point Protocol) connections.
> More information: <https://manned.org/chat.8>.

- Execute a chat script directly from the command line:

`chat '{{expect_send_pairs}}'`

- Execute a chat script from a file:

`chat -f '{{path/to/chat_script}}'`

- Set a custom timeout (in seconds) for expecting a response:

`chat -t {{timeout_in_seconds}} '{{expect_send_pairs}}'`

- Enable verbose output to log the conversation to `syslog`:

`chat -v '{{expect_send_pairs}}'`

- Use a report file to log specific strings received during the conversation:

`chat -r {{path/to/report_file}} '{{expect_send_pairs}}'`

- Dial a phone number using a variable, substituting `\T` in the script:

`chat -T '{{phone_number}}' '{{"ATDT\\T CONNECT"}}'`

- Include an abort condition if a specific string is received:

`chat 'ABORT "{{error_string}}" {{expect_send_pairs}}'`
