# makoctl invoke

> Invoke actions on notifications in mako.
> More information: <https://github.com/emersion/mako> or <https://man.archlinux.org/man/makoctl.1.en>..

- Invoke the default action on the most recent notification:

`makoctl invoke`

- Invoke a specific action on a notification (if not specified, default is used):

`makoctl invoke -n {{notification_id}} {{action_name}}`