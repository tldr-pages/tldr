# prime-run

> Run a program using alternative Nvidia graphics.
> More information: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- Run a program using an Nvidia dedicated GPU:

`prime-run {{command}}`

- Validate whether the Nvidia card is being used:

`prime-run glxinfo | grep "OpenGL renderer"`
