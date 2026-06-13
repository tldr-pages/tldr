# kosmorro

> Compute the ephemerides and the events for a date at a position on Earth.
> More information: <https://kosmorro.space/cli/manpage/>.

- Get ephemerides for Paris, France:

`kosmorro {{[-p|--position]}} "48.7996,2.3511"`

- Get ephemerides for Paris, France, on its timezone:

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-t|--timezone]}} "Europe/Paris"`

- Get ephemerides for Paris, France, on June 9th, 2020:

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-d|--date]}} "2020-06-09"`

- Get ephemerides for Paris, France, in two days:

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-d|--date]}} "+2d"`

- Generate a PDF (Note: TeXLive must be installed):

`kosmorro {{[-o|--output]}} "{{path/to/file}}.pdf"`
