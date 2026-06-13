# tgutil

> Manage a Telegram account.
> See also: `tgcloud`, `tgsend`, `tginfo`.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Edit the last text message on a chat with new text:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} edit --text "{{current_text}}" --newtext "{{new_text}}"`

- Edit all text messages that contain `current_text` with `new_text`:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} editall --text "{{current_text}}" --newtext "{{new_text}}"`

- Delete the last text message on a chat with search value:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} delete --text "{{current_text}}"`

- Delete all messages containing the `query` value:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} deleteall --text "{{query}}"`
