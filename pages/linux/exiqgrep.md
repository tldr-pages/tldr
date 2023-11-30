# exiqgrep

> Perl script offering possibilities to `grep` in the Exim queue output.
> More information: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- Match the sender address using a case-insensitive search:

`exiqgrep -f '<{{email@somedomain.com}}>'`

- Match the sender address and display message IDs only:

`exiqgrep -i -f '<{{email@somedomain.com}}>'`

- Match the recipient address:

`exiqgrep -r '{{email@somedomain.com}}'`

- Remove all messages matching the sender address from the queue:

`exiqgrep -i -f '<{{email@somedomain.com}}>' | xargs exim -Mrm`

- Test for bounced messages:

`exiqgrep -f '^<>$'`

- Display the count of bounced messages:

`exiqgrep -c -f '^<>$'`
