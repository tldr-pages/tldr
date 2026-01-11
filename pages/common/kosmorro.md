# kosmorro

> Compute the ephemerides and the events for a date at a position on Earth.
> More information: <https://kosmorro.space/cli/manpage/>.

- Get ephemerides for Paris, France:

`kosmorro --position={{"48.7996,2.3511"}}`

- Get ephemerides for Paris, France, on its timezone:

`kosmorro --position={{"48.7996,2.3511"}} --timezone={{"Europe/Paris"}}`

- Get ephemerides for Paris, France, on June 9th, 2020:

`kosmorro  --position={{"48.7996,2.3511"}} --date={{"2020-06-09"}}`

- Get ephemerides for Paris, France, in two days:

`kosmorro  --position={{"48.7996,2.3511"}} --date={{"+2d"}}`

- Generate a PDF (Note: TeXLive must be installed):

`kosmorro --output="{{path/to/file.pdf}}"`
