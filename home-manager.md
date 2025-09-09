# home-manager

> Gerencie um ambiente por usuário usando Nix, permitindo configuração declarativa da home do usuário.
> Mais informações:  <https://github.com/nix-community/home-manager>.

- Construir a configuração definida em `~/.config/nixpkgs/home.nix` sem aplicá-la:

`home-manager build`

- Construir e aplicar (switch to) a nova configuração:

`home-manager switch`

- Retroceder de volta para a configuração de uma geração prévia:

`home-manager rollback`

- Listar todas as configurações de gerações existentes:

`home-manager generations`

- Quando estiver usando flakes, execute qualquer operação que requira nix para a execução (build, switch, news) passando o caminho para o flake:

`home-manager {{command}} --flake {{path/to/flake}}`
