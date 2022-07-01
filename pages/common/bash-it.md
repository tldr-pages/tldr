# bash-it

> A collection of community contributed Bash commands and scripts for Bash 3.2+.
> More information: <https://bash-it.readthedocs.io/en/latest/>.

- Update Bash-it to the latest stable/development version:

`bash-it update {{stable|dev}}`

- Reload Bash profile (set `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` to non-empty value for an automatic reload):

`bash-it reload`

- Restart Bash:

`bash-it restart`

- Reload Bash profile with enabled error and warning logging:

`bash-it doctor`

- Reload Bash profile with enabled error/warning/entire logging:

`bash-it doctor {{errors|warnings|all}}`

- Search for Bash-it aliases/plugins/completions:

`bash-it search {{alias|plugin|completion}}`

- Search for Bash-it aliases/plugins/completions and enable/disable all found items:

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
