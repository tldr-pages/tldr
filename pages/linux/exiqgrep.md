# exiqgrep

> The `exiqgrep` utility is a Perl script offering possibilities to `grep` in the Exim queue output.
> More information: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- Match the sender address using a case-insensitive search:

`exiqgrep -f '<{{email@somedomain.com}}>'`

- Match the sender address, display  message ids only:

`exiqgrep -i -f '<{{email@somedomain.com}}>'`

- Match the recipient address:

`exiqgrep -r '{{email@somedomain.com}}'`

- Remove from queue all messages, matching sender address:

`exiqgrep -i -f '<{{email@somedomain.com}}>' | xargs exim -Mrm`

- Test for bounced messages:

`exiqgrep -f '^<>$'`

- Display bounced messages count:

`exiqgrep -c -f '^<>$'`
