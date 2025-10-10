# mvn compile

> Compila o código-fonte de um projeto Maven.
> Mais informações: <https://manned.org/mvn>.

---

- Compila o código-fonte do projeto:

`mvn compile`

- Limpa os arquivos compilados e, em seguida, recompila:

`mvn clean compile`

- Compila um módulo específico em um projeto multi-módulo:

`mvn compile {{[-pl|--projects]}} {{nome_do_modulo}}`

- Pula os testes durante a compilação:

`mvn compile {{[-D|--define]}} skipTests`
