# sfc 

>  Verifica e repara arquivos corrompidos do sistema.
>  Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- Verifica integridade dos arquivos do sistema:
`sfc /scannow`

- Verifica sem corrigir automaticamente:
`sfc /verifyonly`

- Executa no modo offline:
`sfc /scannow /offbootdir={{C:\}} /offwindir={{C:\Windows}}`
   


