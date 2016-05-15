# tldr

[![Build Status][travis-image]][travis-url]
[![Gitter chat][gitter-image]][gitter-url]
[![Issue Stats][issuestats-image]][issuestats-url]

[travis-url]: https://travis-ci.org/tldr-pages/tldr
[travis-image]: https://travis-ci.org/tldr-pages/tldr.svg?branch=master
[gitter-url]: https://gitter.im/tldr-pages/tldr
[gitter-image]: https://badges.gitter.im/tldr-pages/tldr.svg
[issuestats-url]: http://issuestats.com/github/tldr-pages/tldr
[issuestats-image]: http://issuestats.com/github/tldr-pages/tldr/badge/pr?style=flat

A collection of simplified and community-driven man pages.

Install it with `npm install -g tldr` or [try the web client](https://ostera.github.io/tldr.jsx).

## What is tldr?

New to the command-line world? Or just a little rusty?
Or perhaps you can't always remember the arguments to `lsof`, or `tar`?

Maybe it doesn't help that the first option explained in `man tar` is:

```
-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
```

Surely people could benefit from simplified man pages focused on practical examples. How about:

![tldr screenshot](http://raw.github.com/tldr-pages/tldr/master/screenshot.png)

This repository is just that: an ever-growing collection of examples
for the most common UNIX / Linux / OSX / SunOS commands.

## Clients

You can access these pages on your computer using one of the following clients:

- Android clients:
  - [tldr-viewer](https://github.com/gianasista/tldr-viewer), available on
    [Google Play](https://play.google.com/store/apps/details?id=de.gianasista.tldr_viewer)
  - [tldroid](https://github.com/hidroh/tldroid), available on
    [Google Play](https://play.google.com/store/apps/details?id=io.github.hidroh.tldroid)
- [Bash client](https://github.com/raylee/tldr)
- [C++ client](https://github.com/tldr-pages/tldr-cpp-client): `brew install tldr-pages/tldr/tldr`
- [Crystal client](https://github.com/porras/tlcr): `brew install porras/tap/tlcr`
- [Dart client](https://github.com/hterkelsen/tldr): `pub global activate tldr`
- [Elixir client](https://github.com/tldr-pages/tldr_elixir_client) (binaries not yet available)
- [Emacs client](https://github.com/kuanyui/tldr.el)
- [Go client](https://github.com/pranavraja/tldr): `go get github.com/pranavraja/tldr` (or [platform binaries](https://github.com/pranavraja/tldr/releases))
- iOS clients:
  - [tldr-man-page](https://github.com/freesuraj/TLDR), available on [App Store](https://appsto.re/sg/IQ0-_.i)
  - [tldr-pages](https://github.com/mflint/ios-tldr-viewer), available on [App Store](https://itunes.apple.com/us/app/tldt-pages/id1071725095?ls=1&mt=8)
- [Node.js client](https://github.com/tldr-pages/tldr-node-client) : `npm install -g tldr`
- [Perl5 client](https://github.com/shoichikaji/perl-tldr): `cpanm App::tldr`
- Python clients:
  - [tldr-python-client](https://github.com/tldr-pages/tldr-python-client) : `pip install tldr`
  - [tldr.py](https://github.com/lord63/tldr.py): `pip install tldr.py`
- [R client](https://github.com/kirillseva/tldrrr): `devtools::install_github('kirillseva/tldrrr')`
- [Ruby client](https://github.com/YellowApple/tldrb): `gem install tldrb`
- Rust clients:
    - [rust-tldr](https://github.com/rilut/rust-tldr) (online lookup): `cargo install tldr`
    - [tealdeer](https://github.com/dbrgn/tealdeer) (fully featured client with offline cache): `cargo install tealdeer`
- [Web client](https://github.com/ostera/tldr.jsx): https://ostera.github.io/tldr.jsx

There is also a comprehensive [list of clients in our Wiki](https://github.com/tldr-pages/tldr/wiki/TLDR-clients).

## Contributing

- Your favourite command isn't covered?
- You can think of more examples for an existing command?

Contributions are most welcome!
Have a look at the [contributing guidelines](https://github.com/tldr-pages/tldr/blob/master/CONTRIBUTING.md)
and go ahead!

## Similar projects

- [Cheat](https://github.com/chrisallenlane/cheat) allows you to create and view interactive cheatsheets on the command-line.
  It was designed to help remind *nix system administrators of options for commands that they use frequently, but not frequently enough to remember.

- [Bro pages](http://bropages.org/) are a highly readable supplement to man pages.
  Bro pages show concise, common-case examples for Unix commands.

## What does "tldr" mean?

TL;DR stands for "Too Long; Didn't Read".
It originates in Internet slang, where it is used to indicate parts of the text skipped as too lengthy.
Read more in the [TLDR article on Wikipedia](https://en.wikipedia.org/wiki/TL;DR).
