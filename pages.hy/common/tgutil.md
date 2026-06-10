# tgutil

> Կառավարեք Telegram հաշիվը:.
> Տես նաև՝ `tgcloud`, `tgsend`, `tginfo`:.
> Լրացուցիչ տեղեկություններ. <https://pypi.org/project/telegram-cloud/>:.

- Խմբագրել վերջին տեքստային հաղորդագրությունը չաթում նոր տեքստով.:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} edit --text "{{current_text}}" --newtext "{{new_text}}"`

- Խմբագրել բոլոր տեքստային հաղորդագրությունները, որոնք պարունակում են `current_text` `new_text`-ով:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} editall --text "{{current_text}}" --newtext "{{new_text}}"`

- Ջնջել որոնման արժեքով վերջին տեքստային հաղորդագրությունը.:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} delete --text "{{current_text}}"`

- Ջնջել `query` արժեքը պարունակող բոլոր հաղորդագրությունները.:

`tgutil {{[-n|--name]}} {{session_name}} {{[-u|--username]}} {{chat_id}} {{[-m|--mode]}} deleteall --text "{{query}}"`
