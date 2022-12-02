# vt

> Command-line interface for VirusTotal.
> API key from a VirusTotal account is required for this command.
> More information: <https://github.com/VirusTotal/vt-cli>.

- Scan a specific file for viruses:

`vt scan file {{path/to/file}}`

- Scan a URL for viruses:

`vt scan url {{url}}`

- Display information from a specific analysis:

`vt analysis {{path/to/file}}`

- Download files in encrypted `.zip` format (requires premium account):

`vt download {{path/to/file}} --output {{path/to/directory}} --zip --zip-password {{password}}`

- Initialize or re-initialize `vt` to enter API key interactively:

`vt init`

- Display information about a domain:

`vt domain {{url}}`

- Display information for a specific URL:

`vt url {{url}}`

- Display information for a specific IP address:

`vt domain {{ip_address}}`
