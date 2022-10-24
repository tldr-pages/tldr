# vt

> VirusTotal Command Line Interface.
> API key from a VirusTotal account is required for this command.
> More information: <https://github.com/VirusTotal/vt-cli>.

- Scan a file for viruses:

`vt scan file {{file}}`

- Scan a URL for viruses:

`vt scan url {{url}}`

- Display analysis information:

`vt analysis {{f-id|u-id}}`

- Download files in encrypted `.zip` format (requires premium account):

`vt download {{id}} --output {{path/to/directory}} --zip --zip-password {{string}} `

- Initialize or re-initialize `vt` to enter API key:

`vt init`

- Display information about a domain:

`vt domain {{URL}}`

- Display information for a specific URL:

`vt url {{URL}}`

- Display information for a specific ipaddress:

`vt domain {{ip}}`
