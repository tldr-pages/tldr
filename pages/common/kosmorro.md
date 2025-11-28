# kosmorro

> Compute the ephemerides and the events for a date at a position on Earth.
> More information: <https://github.com/Kosmorro/kosmorro/blob/master/manpage/kosmorro.1.md>.

- Get ephemerides for Paris, France:

`kosmorro {{[-la|--latitude]}} 48.7996 {{[-lo|--longitude]}} 2.3511`

- Get ephemerides for Paris, France, in the UTC+2 timezone:

`kosmorro {{[-la|--latitude]}} 48.7996 {{[-lo|--longitude]}} 2.3511 {{[-t|--timezone]}} 2`

- Get ephemerides for Paris, France, on June 9th, 2020:

`kosmorro {{[-la|--latitude]}} 48.7996 {{[-lo|--longitude]}} 2.3511 {{[-d|--date]}} 2020-06-09`

- Generate a PDF (Note: TeXLive must be installed):

`kosmorro {{[-f|--format]}} pdf {{[-o|--output]}} {{path/to/file.pdf}}`
