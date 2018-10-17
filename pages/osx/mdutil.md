# mdutil

> Manage the metadata stores used by Spotlight for indexing.

- Show the indexing status of the startup volume:

`mdutil -s {{/}}`

- Turn on/off the Spotlight indexing for a given volume:

`mdutil -i {{on|off}} {{path/to/volume}}`

- Erase the metadata stores and restart the indexing process:

`mdutil -E {{path/to/volume}}`
