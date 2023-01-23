# ganache-cli

> A Ganache parancssori változata, a személyes blokkláncod Ethereum fejlesztéshez. További információ: <https://www.trufflesuite.com/ganache>.

- Ganache futtatása:

`ganache-cli`

- Ganache futtatása meghatározott számú fiókkal:

`ganache-cli --accounts={{number_of_accounts}}`

- A Ganache futtatása és az elérhető fiókok alapértelmezés szerinti zárolása:

`ganache-cli --secure`

- Futtassa a Ganache szervert és oldjon fel bizonyos fiókokat:

`ganache-cli --secure --unlock "{{account_private_key1}}" --unlock "{{account_private_key2}}"`

- Futtassa a Ganache-t egy adott számlával és egyenleggel:

`ganache-cli --account="{{account_private_key}},{{account_balance}}"`

- Ganache futtatása alapértelmezett egyenleggel rendelkező számlákkal:

`ganache-cli --defaultBalanceEther={{default_balance}}`

- A Ganache futtatása és az összes kérelem naplózása a `stdout` címen:

`ganache-cli --verbose`
