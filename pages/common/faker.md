# faker

> A Python library and a tool to generate fake data.
> More information: <https://faker.readthedocs.io/en/master/>.

- Show all fake data providers along with examples:

`faker`

- Generate fake data of a specific type:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- Generate a number of fake addresses from Germany or Switzerland:

`faker --repeat {{number}} --lang {{de_DE|de_CH}} address`

- Generate a number of cities in Australia and output them to a file:

`faker --repeat {{number}} --lang {{en_AU}} city -o {{path/to/file.txt}}`

- Generate a number of random HTTP user-agents showing verbose output:

`faker --repeat {{number}} --verbose user_agent`

- Generate a number of domain names and separate each using a comma:

`faker --repeat {{number}} --sep '{{,}}' domain_name`
