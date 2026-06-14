# git instaweb

> GitWeb սերվեր գործարկելու օգնական:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-instaweb>:.

- Գործարկեք GitWeb սերվեր ընթացիկ Git պահոցի համար.:

`git instaweb --start`

- Լսեք միայն localhost-ում.:

`git instaweb --start {{[-l|--local]}}`

- Լսեք կոնկրետ նավահանգստում.:

`git instaweb --start {{[-p|--port]}} {{1234}}`

- Օգտագործեք նշված HTTP դեյմոն.:

`git instaweb --start {{[-d|--httpd]}} {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Նաև ավտոմատ գործարկեք վեբ բրաուզերը.:

`git instaweb --start {{[-b|--browser]}}`

- Դադարեցրեք ներկայումս գործող GitWeb սերվերը.:

`git instaweb --stop`

- Վերագործարկեք ներկայումս գործող GitWeb սերվերը.:

`git instaweb --restart`
