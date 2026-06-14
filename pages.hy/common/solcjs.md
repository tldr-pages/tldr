# solcjs

> Solidity կոմպիլյատորի համար JavaScript կապերի մի շարք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/argotorg/solc-js>:.

- Կազմել կոնկրետ պայմանագիր hex:

`solcjs --bin {{path/to/file.sol}}`

- Կազմել կոնկրետ պայմանագրի ABI.:

`solcjs --abi {{path/to/file.sol}}`

- Նշեք բազային ուղին ներմուծումը լուծելու համար.:

`solcjs --bin --base-path {{path/to/directory}} {{path/to/file.sol}}`

- Նշեք արտաքին կոդ պարունակող մեկ կամ մի քանի ուղիներ.:

`solcjs --bin --include-path {{path/to/directory path/to/file.sol ...}}`

- Օպտիմալացնել ստեղծված բայթ կոդը.:

`solcjs --bin --optimize {{path/to/file.sol}}`
