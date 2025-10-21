# Robocopy

> Cópia robusta de arquivos e pastas.
> Por padrão, os arquivos só serão copiados se a origem e o destino tiverem diferentes carimbos de data/hora ou tamanhos de arquivo diferentes.
Mais informações: https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy

- Copiar todos os arquivos .jpg e .bmp de um diretório para outro:
 robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} {{*.jpg}} {{*.bmp}}

- Copiar todos os arquivos e subdiretórios, incluindo os vazios:
  robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} /E

- Espelhar/Sincronizar um diretório, excluindo tudo o que não existe na origem e incluindo todos os atributos e permissões:
  robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} /MIR /COPYALL

- Copiar todos os arquivos e subdiretórios, ignorando os arquivos da origem que são mais antigos do que os do destino:
  robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} /E /XO

- Listar todos os arquivos com 50 MB ou mais, sem copiá-los:
  robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} /MIN:{{52428800}} /L

- Permitir retomada automática se a conexão de rede for perdida e limitar o número de tentativas a 5 com tempo de espera de 15 segundos entre elas:
 robocopy {{caminho\para\diretorio_origem}} {{caminho\para\diretorio_destino}} /Z /R:5 /W:15

- Exibir ajuda:
  robocopy /?
