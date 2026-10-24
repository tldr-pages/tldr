# gcrane completion

> Genereer het autocompletion script voor gcrane voor de opgegeven shell.
> De beschikbare shells zijn Bash, fish, PowerShell en Zsh.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genereer het autocompletion script voor je shell:

`gcrane completion {{shell_naam}}`

- Zet de completion beschrijvingen uit:

`gcrane completion {{shell_naam}} --no-descriptions`

- Laad completions in je huidige shellsessie (Bash/Zsh):

`source <(gcrane completion bash/zsh)`

- Laad completions in je huidige shellsessie (fish):

`gcrane completion fish | source`

- Laad completions voor elke nieuwe sessie (Bash):

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- Laad completions voor elke nieuwe sessie (Zsh):

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- Laad completions voor elke nieuwe sessie (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Toon de help:

`gcrane completion {{shell_naam}} {{[-h|--help]}}`
