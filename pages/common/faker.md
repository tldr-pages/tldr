# faker

> A Python library and a tool to generate fake data.
> More information: <https://faker.readthedocs.io/en/master/>.

- Show all fake data providers along with examples:

`faker`

- Generate fake data of a specific type:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- Generate a number of fake addresses from a specific country (use `localectl list-locales | cut -d. -f1` to get list of locales):

`faker --repeat {{number}} --lang {{de_DE|de_CH|...}} address`

- Generate a number of cities in a specific country and output them to a file (use `localectl list-locales | cut -d. -f1` to get list of locales):

`faker --repeat {{number}} --lang {{en_AU|en_US|...}} city -o {{path/to/file.txt}}`

- Generate a number of random HTTP user-agents showing verbose output:

`faker --repeat {{number}} --verbose user_agent`

- Generate a number of domain names and separate each using a specific separator:

`faker --repeat {{number}} --sep '{{,}}' domain_name`
