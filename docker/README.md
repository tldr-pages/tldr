# Docker image

Build tldr container with:

```bash
make build
```

Add alias on `~/.bashrc` or `~/.zshrc`: `alias tldr='docker run --rm -it -v ~/.tldr/:/root/.tldr/ nutellinoit/tldr'`

Use `tldr` command
