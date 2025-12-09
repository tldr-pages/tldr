# tgcloud

> Manage a Telegram account.
> See also: `tgsend`, `tginfo`, `tgutil`.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Upload a file to a chat with a caption:

`tgcloud {{[-m|--mode]}} upload {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-p|--path]}} {{path_of_the_file}} {{[-c|--caption]}} {{caption}}`

- Download a file from a chat and store it in `path/to/store` with a caption:

`tgcloud {{[-m|--mode]}} download {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-p|--path]}} {{path/to/store}} {{[-c|--caption]}} {{caption}}`
