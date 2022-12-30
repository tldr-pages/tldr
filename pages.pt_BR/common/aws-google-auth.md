# aws-google-auth

> Linha de comando para obter credenciais (STS) temporárias AWS usando o Google Apps como um provedor (Single Sign-On) federado.
> Mais informações: <https://github.com/cevoaustralia/aws-google-auth>.

- Loga com o Google SSO usando identificadores IDP e SP e criar credenciais com duração de uma hora:

`aws-google-auth -u {{exemplo@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Loga perguntando ([a]sking) qual papel usar (no caso de diversos papeis SAML disponíveis):

`aws-google-auth -u {{examplo@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Resolve aliases para contas AWS:

`aws-google-auth -u {{examplo@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Exibe informações de ajuda:

`aws-google-auth -h`
