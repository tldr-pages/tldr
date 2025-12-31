# gcrane completion

> Genereer het autocompletion script voor gcrane voor de opgegeven shell.
> De beschikbare shells zijn `bash`, `fish`, `powershell` en `zsh`.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genereer het autocompletion script voor je shell:

`gcrane completion {{shell_naam}}`

- Zet de completion beschrijvingen uit:

`gcrane completion {{shell_naam}} --no-descriptions`

- Laad completions in je huidige shellsessie (bash/zsh):

`source <(gcrane completion bash/zsh)`

- Laad completions in je huidige shellsessie (fish):

`gcrane completion fish | source`

- Laad completions voor elke nieuwe sessie (bash):

`gcrane completion bash > /etc/bash_completion.d/gcrane`

- Laad completions voor elke nieuwe sessie (zsh):

`gcrane completion zsh > "${fpath[1]}/_gcrane"`

- Laad completions voor elke nieuwe sessie (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Toon de help:

`gcrane completion {{shell_naam}} {{[-h|--help]}}`
