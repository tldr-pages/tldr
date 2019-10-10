tldr
Build status Gitter chat Merged PRs Issue stats GitHub contributors license

A collection of simplified and community-driven man pages.

Install it with npm install -g tldr or try the web client.

What is tldr?
New to the command-line world? Or just a little rusty? Or perhaps you can't always remember the arguments to lsof, or tar?

Maybe it doesn't help that the first option explained in man tar is:

-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
Surely people could benefit from simplified man pages focused on practical examples. How about:

tldr screenshot

This repository is just that: an ever-growing collection of examples for the most common UNIX / Linux / macOS / SunOS commands.

Clients
You can access these pages on your computer using one of the following clients:

Alfred Workflow
Android clients:
tldroid, available on Google Play (outdated)
Bash clients:
tldr
tldr-bash-client
C# client
C++ client: brew install tldr
Chrome Extension available on Chrome Web Store
Crystal client: brew install porras/tap/tlcr
Dart client: pub global activate tldr
Dash docset: Open Preferences > Downloads > User Contributed and find tldr pages in the list
Docker images:
tldr-docker- Run the tldr command via a docker container: alias tldr='docker run --rm -it -v ~/.tldr/:/root/.tldr/ nutellinoit/tldr'
Elixir client (binaries not yet available)
Emacs client, available on MELPA
Go clients:
github.com/pranavraja/tldr: go get github.com/pranavraja/tldr (or platform binaries)
4d63.com/tldr: go get 4d63.com/tldr or brew install 4d63/tldr/tldr (or platform binaries)
github.com/elecprog/tldr: go get github.com/elecprog/tldr (or platform binaries)
github.com/isacikgoz/tldr: go get github.com/isacikgoz/tldr (or platform binaries)
iOS clients:
tldr-man-page, available on App Store
tldr-pages, available on App Store
Haskell client: stack install tldr
Node.js client: npm install -g tldr
OCaml client: opam install tldr
Perl5 client: cpanm App::tldr
PHP client: composer global require brainmaestro/tldr
Python clients:
tldr-python-client: pip install tldr or pacman -S tldr on Arch Linux
tldr.py: pip install tldr.py
R client: devtools::install_github('kirillseva/tldrrr')
Ruby client: gem install tldrb
Rust clients:
DistroWatch
There is also a comprehensive list of clients in our Wiki.

Contributing
Your favourite command isn't covered?
You can think of more examples for an existing command?
Contributions are most welcome! We strive to maintain a welcoming and collaborative community. Have a look at the contributing guidelines, and go ahead!

Similar projects
Cheat allows you to create and view interactive cheatsheets on the command-line. It was designed to help remind *nix system administrators of options for commands that they use frequently, but not frequently enough to remember.

Bro pages are a highly readable supplement to man pages. Bro pages show concise, common-case examples for Unix commands. The examples are submitted by the user base, and can be voted up or down; the best entries are what people see first when they look up a command.

eg provides detailed examples with explanations on the command line. Examples come from the repository, but eg supports displaying custom examples and commands alongside the defaults.

What does "tldr" mean?
TL;DR stands for "Too Long; Didn't Read". It originates in Internet slang, where it is used to indicate that a long text (or parts of it) has been skipped as too lengthy. Read more in Wikipedia's TL;DR article.
