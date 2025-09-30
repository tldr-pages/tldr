# exiqgrep

> Perl script offering possibilities to `grep` in the Exim queue output.
> More information: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- Match the sender address using a case-insensitive search:

`exiqgrep -f '<{{email@example.com}}>'`

- Match the sender address and display message IDs only:

`exiqgrep -i -f '<{{email@example.com}}>'`

- Match the [r]ecipient address:

`exiqgrep -r '{{email@example.com}}'`

- Remove all messages matching the sender address from the queue:

`exiqgrep -i -f '<{{email@example.com}}>' | xargs exim -Mrm`

- Test for bounced messages:

`exiqgrep -f '^<>$'`

- Display the [c]ount of bounced messages:

`exiqgrep -c -f '^<>$'`
