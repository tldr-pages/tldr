# git-sh-i18n

> Load internationalization helper functions into Git shell scripts.
> Not meant for end user; provides wrappers to be implemented in later versions.
> More information: <https://git-scm.com/docs/git-sh-i18n>.

- Source the script:

`. "$(git --exec-path)/git-sh-i18n"`

- Translate strings:

`gettext "{{Pushing feature-branch...}}"`

- Translate strings with variables:

`eval_gettext "{{Pushing \$branch_name...}}"`
