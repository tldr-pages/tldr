# telegram-cloud

> Use this Python package for Telegram to download, upload, and manage your Telegram account on the Command Line Interface (CLI).
> More information: <https://pypi.org/project/telegram-cloud/>.

- To login to your telegram account:

`tglogin`

- Upload file to chat with caption:

`tgcloud --mode upload --name {{session_name}} --username {{chat_id}} --path {{path_of_the_file}} --caption {{caption}}`

- Download file from chat and store it in `path_to_store` with caption:

`tgcloud -m download -n {{session_name}} -u {{chat_id}} -p {{path_to_store}} -c {{caption}}`

- Send message to chat:

`tgsend --name {{session_name}} --username {{chat_id}} "MESSAGE TO SEND"`

- Search all PDFs inside a telegram conversation:

`tginfo --name {{session_name}} --username {{chat_id}} --search "SEARCH VALUE / FILE EXTENSION"`

- Edit the last text message on chat with new text (`--mode editall` to edit all message with `current_text`):

`tgutil -n {{session_name}} -u {{chat_id}} --mode edit --text "CURRENT TEXT" --newtext "NEW TEXT"`

- Get info for all Media inside a telegram chat:

`tginfo -n {{session_name}} -u {{chat_id}}`
