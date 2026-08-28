# timekpra

> Command-line administration client for Timekpr-nExT, a tool to manage and limit computer usage time per user account.
> Automatically falls back to this CLI mode when no graphical display is available.
> More information: <https://mjasnik.gitlab.io/timekpr-next/>.

- List all users known to Timekpr-nExT:

`timekpra --getuserlist`

- Show the stored configuration and time information for a user:

`timekpra --getuserinfo {{username}}`

- Show real-time configuration and time information for a user:

`timekpra --getuserinfort {{username}}`

- Set the allowed days of the week for a user (e.g. Monday to Friday):

`timekpra --setalloweddays {{username}} '{{1;2;3;4;5}}'`

- Set daily time limits for each allowed day:

`timekpra --settimelimits {{username}} '{{2h;2h;2h;2h;3h}}'`

- Set the weekly time limit for a user:

`timekpra --settimelimitweek {{username}} {{13h53m20s}}`

- Add, subtract, or set a user's remaining time for today:

`timekpra --settimeleft {{username}} {{+|-|=}} {{30m}}`

- Set the lockout action applied once a user's time runs out:

`timekpra --setlockouttype {{username}} {{lock|suspend|terminate|shutdown}}`
