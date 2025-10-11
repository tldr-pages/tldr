# tgutil

> Manage a Telegram account.
> See also: `tgcloud`, `tgsend`, `tginfo`.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Edit the last text message on chat with new text (`--mode editall` to edit all message with `current_text`):

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} edit --text "CURRENT TEXT" --newtext "NEW TEXT"`

- Delete the last text message on chat with search value (`--mode deleteall` to delete all message with search value):

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} delete --text "CURRENT TEXT" --newtext "NEW TEXT"`
