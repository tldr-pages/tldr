# tripwire

> Monitor file and directory integrity.
> Requires configuration, signing keys, and a policy before initializing the database.
> More information: <https://manned.org/tripwire>.

- Initialize the database using the configured policy:

`sudo tripwire {{[-m i|--init]}}`

- Check monitored files and directories for changes:

`sudo tripwire {{[-m c|--check]}}`

- Check a specific file or directory listed in the policy:

`sudo tripwire {{[-m c|--check]}} {{path/to/file_or_directory}}`

- Update the policy using a text policy file:

`sudo tripwire {{[-m p|--update-policy]}} {{path/to/policy.txt}}`

- Display detailed help for all modes:

`tripwire --help all`
