# Conda որոնում

> Փնտրեք փաթեթներ և ցույց տվեք դրանց մանրամասները:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/search.html>:.

- Որոնել կոնկրետ փաթեթ.:

`conda search {{package_name}}`

- Փնտրեք փաթեթ դրա մանրամասների հետ միասին.:

`conda search {{package_name}} {{[-i|--info]}}`

- Փաթեթի անվան մեջ որոնեք `string` պարունակող փաթեթներ.:

`conda search "*string*"`

- Փաթեթի հատուկ տարբերակի որոնում.:

`conda search "{{package_name}}>={{package_version}}"`

- Փաթեթի որոնում կոնկրետ ալիքում.:

`conda search {{channel}}::{{package_name}}`

- Որոնեք, եթե փաթեթը տեղադրված է որևէ տեղական միջավայրում.:

`conda search --envs {{package_name}}`
