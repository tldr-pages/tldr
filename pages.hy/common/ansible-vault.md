# ansible-ի պահոց

> Գաղտնագրել և վերծանել արժեքները, տվյալների կառուցվածքները և ֆայլերը Ansible նախագծերում:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>:.

- Ստեղծեք նոր կոդավորված պահոցային ֆայլ՝ գաղտնաբառի հուշումով.:

`ansible-vault create {{path/to/vault_file}}`

- Խմբագրել, դիտել կամ վերաբանալ (վերածագրել) գոյություն ունեցող գաղտնագրված պահոցային ֆայլը՝ գաղտնաբառի հուշումով.:

`ansible-vault {{edit|view|rekey}} {{path/to/vault_file}}`

- Ստեղծեք նոր կոդավորված պահոցային ֆայլ՝ օգտագործելով գաղտնաբառի ֆայլ՝ այն կոդավորելու համար.:

`ansible-vault create --vault-password-file {{path/to/password_file}} {{path/to/vault_file}}`

- Կոդավորեք գոյություն ունեցող պարզ տեքստային ֆայլը տեղում՝ օգտագործելով գաղտնաբառի ֆայլը.:

`ansible-vault encrypt --vault-password-file {{path/to/password_file}} {{path/to/file}}`

- Կոդավորեք տողը՝ օգտագործելով Ansible-ի գաղտնագրված տողային ձևաչափը՝ ցուցադրելով ինտերակտիվ հուշումներ.:

`ansible-vault encrypt_string`

- Դիտեք կոդավորված պահոցային ֆայլը՝ օգտագործելով գաղտնաբառի ֆայլ՝ ապակոդավորելու համար.:

`ansible-vault view --vault-password-file {{path/to/password_file}} {{path/to/vault_file}}`

- Վերաբանալին (վերակոդավորումը) արդեն գաղտնագրված պահոցային ֆայլը նոր գաղտնաբառի ֆայլով.:

`ansible-vault rekey --vault-password-file {{path/to/old_password_file}} --new-vault-password-file {{path/to/new_password_file}} {{path/to/vault_file}}`
