# npm հնացած

> Նշեք `npm` փաթեթի տարբերակը կամ տարբերակների շրջանակը որպես հնացած:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-deprecate/>:.

- Հնազանդեցնել փաթեթի կոնկրետ տարբերակը.:

`npm deprecate {{package_name}}@{{version}} "{{deprecation_message}}"`

- Հնեցրեք փաթեթի մի շարք տարբերակներ.:

`npm deprecate {{package_name}}@"<{{version_range}}" "{{deprecation_message}}"`

- Փաթեթի որոշակի տարբերակի հնազանդումը.:

`npm deprecate {{package_name}}@{{version}} ""`
