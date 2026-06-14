# nix eval

> Գնահատեք Nix արտահայտությունը և արդյունքը տպեք `stdout`-ում:.
> Լրացուցիչ տեղեկություններ. <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-eval.html>:.

- Գնահատեք Nix flake հատկանիշները ընթացիկ գրացուցակում.:

`nix eval .#{{attributes}}`

- Գնահատեք Nix-ի տրված արտահայտությունը.:

`nix eval --expr '{{your_expression}}'`

- Գնահատեք Nix արտահայտությունը նշված ֆայլից.:

`nix eval --file {{path/to/file}}`

- Տպեք նշված փաթեթի խանութի ուղին nixpkgs-ից.:

`nix eval {{nixpkgs#pkg}} --raw`

- Գնահատեք ատրիբուտները փաթիլից անմիջապես GitHub-ից.:

`nix eval {{github:owner/repo#attributes}}`

- Գնահատեք տրված լամբդա ֆունկցիան, որն անցնում է նշված փաթեթը որպես փաստարկ.:

`nix eval {{nixpkgs#pkg}} --apply '{{lambda_function}}'`
