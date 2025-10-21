# sfc 

>  Verifica e repara arquivos corrompidos do sistema.
>  Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- Verifica integridade dos arquivos do sistema:
`sfc /scannow`

- Verificar sem corrigir automaticamente:
`sfc /verifyonly`

- Executar no modo offline:
`sfc /scannow /offbootdir={{C:\}} /offwindir={{C:\Windows}}`
   


