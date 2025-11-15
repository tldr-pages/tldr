# clock

> Set the system clock.
> More information: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- Enter privileged execution mode:

`clock set {{23}}:{{59}}:{{59}} {{31}} {{april}} {{2000}}`

- Auto negotiate with the far end of the link, defaulting to active-clock:

`clock active prefer`

- Auto negotiate with the far end of the link, defaulting to passive-clock:

`clock passive prefer`

- Show the current clock mode negotiated by the firmware:

`clock show interfaces`
