# bash-it

> Bash-it is a collection of community Bash commands and scripts for Bash 3.2+.
> More information: <https://bash-it.readthedocs.io/en/latest/>.

- Update Bash-it version to the latest stable/development one:

`bash-it update {{stable|dev}}`

- Reload Bash profile (set `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` to non-empty value for an automatic reload):

`bash-it reload`

- Restart Bash entirely:

`bash-it restart`

- Reload Bash profile with enabled error and warning logging:

`bash-it doctor`

- Reload Bash profile with enabled error/warning/entire logging:

`bash-it doctor {{errors|warnings|all}}`
