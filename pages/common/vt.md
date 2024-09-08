# vt

> Command-line interface for VirusTotal.
> API key from a VirusTotal account is required for this command.
> More information: <https://github.com/VirusTotal/vt-cli>.

- Scan a specific file for viruses:

`vt scan file {{path/to/file}}`

- Scan a URL for viruses:

`vt scan url {{url}}`

- Display information from a specific analysis:

`vt analysis {{file_id|analysis_id}}`

- Download files in encrypted Zip format (requires premium account):

`vt download {{file_id}} --output {{path/to/directory}} --zip --zip-password {{password}}`

- Initialize or re-initialize `vt` to enter API key interactively:

`vt init`

- Display information about a domain:

`vt domain {{url}}`

- Display information for a specific URL:

`vt url {{url}}`

- Display information for a specific IP address:

`vt domain {{ip_address}}`
