
# robocopy

> Copia arquivos e pastas de forma robusta:
>  Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Copiar arquivos de uma pasta para outra:
`robocopy {{origem}} {{destino}}`

- Copiar subpastas tambem:
`robocopy {{origem}} {{destino}} /e`

- Espelhar uma pasta (excluir no destino o que não existe na origem):
`robocopy {{origem}} {{destino}} /mir`

- Copiar apenas arquivos modificados:
`robocopy {{origem}} {{destino}} /xo`

  
