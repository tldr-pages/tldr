# dumpzilla

> Forensic tool to extract information from Firefox, Iceweasel and Seamonkey browsers.
> More information: <https://www.dumpzilla.org>.

- Gather summary data from browser profile.

`dumpzilla {{path/to/browser_profile}} --summary`

- Extract everything except the DOM data.

`dumpzilla {{path/to/browser_profile}} --All`

- Extract all stored passwords in browser profile.

`dumpzilla {{path/to/browser_profile}} --Passwords`

- Extract complete listing of browser download history.

`dumpzilla {{path/to/browser_profile}} --Downloads`

- Extract complete listing of browser bookmarks.

`dumpzilla {{path/to/browser_profile}} --Bookmarks`
