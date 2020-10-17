# calendar

> Display upcoming events from a calendar file.
> Basic event format: "(month)/(day)	(Description)" (tab-separated).

- Show events for today and tomorrow (or the weekend on Friday) from the default calendar:

`calendar`

- Look [A]head, showing events for the next 7 days:

`calendar -A 7`

- Look [B]ack, showing events for the previous 7 days:

`calendar -B 7`

- Show events from a custom calendar file:

`calendar -f {{/path/to/calendar_file}}`

- Example entry for Christmas:

`12/25   Christmas`

- Example entry for US Thanksgiving (4th Thursday of November):

`11/ThuFourth    Thanksgiving`

- Example entry for US Memorial Day (last Monday of May):

`May MonLast      Memorial Day`
