# telegram-cloud

> It's a python package for Telegram, which can give you an ability to download, upload, and more options to do with your Telegram account on CLI.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Installation :

`pip3 install telegram-cloud`

- To login to your telegram account:

`tglogin`

- Upload file to chat with caption:

`tgcloud -m upload -n {{session_name}} -u {{chat_id}} -p {{path_of_the_file}} -c {{caption}}`

- Download file from chat and store it in `path_to_store` with caption:

`tgcloud -m download -n {{session_name}} -u {{chat_id}} -p {{path_to_store}} -c {{caption}}`

- Send message to chat:

`tgsend -n {{session_name}} -u {{chat_id}} "MESSAGE TO SEND"`

- Search all PDFs inside a telegram conversation:

`tginfo -n {{session_name}} -u {{chat_id}} -s "SEARCH VALUE / FILE EXTENSION"`

- Edit the last text message on chat with new text (`--mode editall` to edit all message with `current_text`):

`tgutil -n {{session_name}} -u {{chat_id}} --mode edit --text "CURRENT TEXT" --newtext "NEW TEXT"`

- Get info for all Media inside a telegram chat:

`tginfo -n {{session_name}} -u {{chat_id}}`
