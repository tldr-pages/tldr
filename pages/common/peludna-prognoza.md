# peludna-prognoza

> Fetch pollen measurement data for Croatian cities from your terminal using Pliva's allergies data API.
> More information: <https://github.com/vladimyr/peludna-prognoza>.

- Start an interactive search for a city and fetch data for it:

`peludna-prognoza`

- Fetch data for a city:

`peludna-prognoza "{{city}}"`

- Display data in a machine-readable format:

`peludna-prognoza "{{city}}" --{{json|xml}}`

- Display the pollen measurement page for a city at <https://plivazdravlje.hr> in the default web browser:

`peludna-prognoza "{{city}}" --web`
