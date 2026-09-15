# pkexec

> Executa comandos como outro usuário.
> Pede por uma senha em uma interface gráfica se disponível.
> Veja também: `sudo`, `run0`, `doas`.
> Mais informações: <https://polkit.pages.freedesktop.org/polkit/pkexec.1.html>.

- Executa um comando como root:

`pkexec {{comando}}`

- Muda para o usuário root:

`pkexec`

- Executa um comando como um usuário específico:

`pkexec --user {{usuário}} {{comando}}`
