# ծանուցել-ուղարկել

> Ծանուցում ստեղծելու համար օգտագործեք ընթացիկ աշխատասեղանի միջավայրի ծանուցման համակարգը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/notify-send>:.

- Ցույց տալ ծանուցում «Թեստ» վերնագրով և «Սա թեստ է» բովանդակությամբ.:

`notify-send "Test" "This is a test"`

- Ցուցադրել ծանուցում հատուկ պատկերակով.:

`notify-send {{[-i|--icon]}} {{icon.png}} "{{Test}}" "{{This is a test}}"`

- Ցույց տալ ծանուցում 5 վայրկյան.:

`notify-send {{[-t|--expire-time]}} 5000 "{{Test}}" "{{This is a test}}"`

- Ցույց տալ ծանուցում նշված հրատապության մակարդակով (կանխադրված՝ նորմալ).:

`notify-send {{[-u|--urgency]}} {{low|normal|critical}} "{{Test}}" "{{This is a test}}"`

- Ցույց տալ ծանուցում հավելվածի պատկերակով և անունով.:

`notify-send "{{Test}}" {{[-i|--icon]}} {{google-chrome}} {{[-a|--app-name]}} "{{Google Chrome}}"`
