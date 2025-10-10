# faker

> Uma biblioteca e ferramenta Python para gerar dados falsos.
> Mais informações: <https://faker.readthedocs.io/en/master/>.

---

### Exemplos de Uso

- **Mostra todos os provedores** de dados falsos juntamente com exemplos:

`faker`

- **Gera dados falsos** de um tipo específico:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- **Gera endereços falsos** de um país específico:
  *(Use `localectl list-locales | cut --delimiter . --fields 1` para obter a lista de locales.)*

`faker {{[-r|--repeat]}} {{number}} {{[-l|--lang]}} {{de_DE|de_CH|...}} address`

- **Gera cidades** em um país específico e as **salva em um arquivo**:
  *(Use `localectl list-locales | cut --delimiter . --fields 1` para obter a lista de locales.)*

`faker {{[-r|--repeat]}} {{number}} {{[-l|--lang]}} {{en_AU|en_US|...}} city -o {{caminho/para/arquivo.txt}}`

- **Gera user-agents HTTP** aleatórios, mostrando a **saída detalhada** (*verbose*):

`faker {{[-r|--repeat]}} {{number}} {{[-v|--verbose]}} user_agent`

- **Gera nomes de domínio** e separa cada um usando um **separador** específico:

`faker {{[-r|--repeat]}} {{number}} {{[-s|--sep]}} '{{,}}' domain_name`
