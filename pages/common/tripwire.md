# tripwire

> Monitor file and directory integrity.
> Requires configuration, signing keys, and a policy before initializing the database.
> More information: <https://github.com/Tripwire/tripwire-open-source>.

- Initialize the database using the configured policy:

`sudo tripwire --init`

- Check monitored files and directories for changes:

`sudo tripwire --check`

- Check a specific file or directory listed in the policy:

`sudo tripwire --check {{path/to/file_or_directory}}`

- Update the policy using a text policy file:

`sudo tripwire --update-policy {{path/to/policy.txt}}`

- Display detailed help for all modes:

`tripwire --help all`
