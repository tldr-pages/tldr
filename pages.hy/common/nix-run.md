# nix վազում

> Գործարկեք հավելված Nix փաթիլից:.
> Տես նաև՝ `nix flake`:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-run.html>:.

- Գործարկեք լռելյայն հավելվածը ընթացիկ գրացուցակի փաթիլում.:

`nix run`

- Գործարկեք հրաման, որի անունը համընկնում է nixpkgs-ի փաթեթի անվան հետ (եթե ցանկանում եք այդ փաթեթից տարբեր հրամաններ ունենալ, տես `tldr nix shell`):

`nix run nixpkgs#{{pkg}}`

- Գործարկեք հրաման՝ տրված փաստարկներով.:

`nix run nixpkgs#{{vim}} -- {{path/to/file}}`

- Գործարկել հեռավոր պահոցից.:

`nix run {{remote_name}}:{{owner}}/{{repository}}`

- Գործարկեք հեռավոր պահոցից՝ օգտագործելով հատուկ պիտակ, վերանայում կամ մասնաճյուղ.:

`nix run {{remote_name}}:{{owner}}/{{repository}}/{{reference}}`

- Գործարկեք հեռավոր պահոցից՝ նշելով ենթացուցակ և ծրագիր.:

`nix run "{{remote_name}}:{{owner}}/{{repository}}?dir={{dir_name}}#{{app}}"`

- Գործարկեք GitHub-ի ձգման հարցումը.:

`nix run github:{{owner}}/{{repository}}/pull/{{number}}/head`
