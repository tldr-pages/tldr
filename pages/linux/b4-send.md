# b4 send

> Send a patch series prepared with `b4 prep` to a mailing list.
> More information: <https://b4.docs.kernel.org/en/latest/contributor/send.html>.

- Send patches from the current prep-tracked branch:

`b4 send`

- Generate the messages to review without sending them:

`b4 send {{[-o|--output-dir]}} {{path/to/directory}}`

- Send patches to specific recipients for preview without rerolling the series version:

`b4 send --preview-to {{email_address1 email_address2 ...}}`

- Send a previously sent version of the series again:

`b4 send --resend {{version_number}}`

- Perform a dry run without sending any mail:

`b4 send {{[-d|--dry-run]}}`
