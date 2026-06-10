# bw

> Մուտք գործեք և կառավարեք Bitwarden պահոց:.
> Լրացուցիչ տեղեկություններ. <https://bitwarden.com/help/cli/>:.

- Մուտք գործեք Bitwarden օգտվողի հաշիվ.:

`bw login`

- Դուրս գալ Bitwarden օգտվողի հաշվից.:

`bw logout`

- Որոնել և ցուցադրել իրեր Bitwarden պահոցից.:

`bw list items --search {{github}}`

- Ցուցադրել որոշակի տարր Bitwarden պահոցից.:

`bw get item {{github}}`

- Ստեղծեք թղթապանակ Bitwarden պահոցում.:

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`
