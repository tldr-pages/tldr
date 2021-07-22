# gsettings

> Query and modify dconf settings with schema validation.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- Set the value of a key. Fails if the key doesn't exist or the value is out of range:

`gsettings set {{org.example.schema}} {{example-key}} {{value}}`

- Print the value of a key or the schema-provided default if the key has not been set in `dconf`:

`gsetings get {{org.example.schema}} {{example-key}}`

- Unset a key, so that its schema default value will be used:

`gsettings reset {{org.example.schema}} {{example-key}}`

- Display all (non-relocatable) schemas, keys, and values:

`gsettings list-recursively`

- Display all keys and values (default if not set) from one schema:

`gsettings list-recursively {{org.example.schema}}`

- Display schema-allowed values for a key (helpful with enum keys):

`gsettings range {{org.example.schema}} {{example-key}}`

- Display the human-readable description of a key:

`gsettings describe {{org.example.schema}} {{example-key}}`
