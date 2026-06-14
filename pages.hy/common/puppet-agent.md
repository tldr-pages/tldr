# տիկնիկային գործակալ

> Առբերում է հաճախորդի կոնֆիգուրացիան Puppet սերվերից և կիրառում այն տեղական հոսթի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/puppetlabs/puppet/blob/main/references/man/agent.md>:.

- Գրանցեք հանգույց Տիկնիկային սերվերում և կիրառեք ստացված կատալոգը.:

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_time}}`

- Գործարկեք գործակալը հետին պլանում (օգտագործում է պարամետրերը `puppet.conf`-ից):

`puppet agent`

- Գործարկեք գործակալը մեկ անգամ առաջին պլանում, ապա դուրս եկեք.:

`puppet agent --test`

- Գործարկեք գործակալը չոր ռեժիմով.:

`puppet agent --test --noop`

- Գրանցեք յուրաքանչյուր գնահատվող ռեսուրս (նույնիսկ եթե ոչինչ չի փոխվում).:

`puppet agent --test --evaltrace`

- Անջատեք գործակալը.:

`puppet agent --disable "{{message}}"`

- Միացնել գործակալին.:

`puppet agent --enable`
