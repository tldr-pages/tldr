# telegram-cloud

> Manage a Telegram account.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Login to a telegram account:

`tglogin`

- Upload file to chat with caption:

`tgcloud {{[-m|--mode]}} upload {{[-n|--name]}}  {{session_name}} {{[-u|--username]}}  {{chat_id}} {{[-p|--path]}}  {{path_of_the_file}} {{[-c|--caption]}}  {{caption}}`

- Download file from chat and store it in `path_to_store` with caption:

`tgcloud {{[-m|--mode]}} download {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-p|--path]}} {{path_to_store}} {{[-c|--caption]}} {{caption}}`

- Send message to chat:

`tgsend {{[-n|--name]}}  {{session_name}} {{[-u|--username]}}  {{chat_id}} "MESSAGE TO SEND"`

- Search all PDFs inside a telegram conversation:

`tginfo {{[-n|--name]}}  {{session_name}} {{[-u|--username]}}  {{chat_id}} {{[-s|--search]}} "SEARCH VALUE / FILE EXTENSION"`

- Edit the last text message on chat with new text (`--mode editall` to edit all message with `current_text`):

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} edit --text "CURRENT TEXT" --newtext "NEW TEXT"`

- Get info for all Media inside a telegram chat:

`tginfo {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}}`
