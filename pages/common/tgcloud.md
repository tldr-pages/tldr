# tgcloud

> Manage a Telegram account.
> See also: `tgsend`, `tginfo`, `tgutil`.
> More information: <https://pypi.org/project/telegram-cloud/>.

- Upload file to chat with caption:

`tgcloud {{[-m|--mode]}} upload {{[-n|--name]}}  {{session_name}} {{[-u|--username]}}  {{chat_id}} {{[-p|--path]}}  {{path_of_the_file}} {{[-c|--caption]}}  {{caption}}`

- Download file from chat and store it in `path_to_store` with caption:

`tgcloud {{[-m|--mode]}} download {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-p|--path]}} {{path_to_store}} {{[-c|--caption]}} {{caption}}`
