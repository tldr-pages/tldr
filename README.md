<div align="center">
  <h1><a href="https://tldr.sh/"><img alt="tldr-pages" src="images/banner.png" width=600/></a></h1>

[![Build status][github-actions-image]][github-actions-url]
[![Gitter chat][gitter-image]][gitter-url]
[![Merged PRs][prs-merged-image]][prs-merged-url]
[![GitHub contributors][contributors-image]][contributors-url]
[![license][license-image]][license-url]

[github-actions-url]: https://github.com/tldr-pages/tldr/actions
[github-actions-image]: https://img.shields.io/github/workflow/status/tldr-pages/tldr/CI.svg
[gitter-url]: https://gitter.im/tldr-pages/tldr
[gitter-image]: https://img.shields.io/badge/chat-on_gitter-deeppink
[prs-merged-url]: https://github.com/tldr-pages/tldr/pulls?q=is:pr+is:merged
[prs-merged-image]: https://img.shields.io/github/issues-pr-closed-raw/tldr-pages/tldr.svg?label=merged+PRs&color=green
[contributors-url]: https://github.com/tldr-pages/tldr/graphs/contributors
[contributors-image]: https://img.shields.io/github/contributors-anon/tldr-pages/tldr.svg
[license-url]: https://github.com/tldr-pages/tldr/blob/main/LICENSE.md
[license-image]: https://img.shields.io/badge/license-CC_BY_4.0-blue.svg
</div>

## What is tldr-pages?

The **tldr-pages** project is a collection of community-maintained help pages
for command-line tools, that aims to be a simpler, more approachable complement
to traditional [man pages](https://en.wikipedia.org/wiki/Man_page).

Maybe you are new to the command-line world? Or just a little rusty?
Or perhaps you can't always remember the arguments to `lsof`, or `tar`?

It certainly doesn't help that the first option explained in `man tar` is:

```
-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
```

There seems to be room for simpler help pages, focused on practical examples.
How about:

![animated svg of the tldr client displaying the tar command](images/tldr.svg)

This repository is just that: an ever-growing collection of examples
for the most common UNIX, Linux, macOS, SunOS and Windows command-line tools.

## How do I use it?

A popular and convenient way to access these pages on your computer
is to install the [Node.js client](https://github.com/tldr-pages/tldr-node-client),
which is supported by the tldr-pages project maintainers:

    npm install -g tldr

You can also use the fully-featured [official Python client](https://github.com/tldr-pages/tldr-python-client) which can be installed via `pip3`.

    pip3 install tldr

That way you can write `tldr tar` in the terminal to show the tldr page for `tar`,
just like you would write `man tar` to show its manpage.

However, if you just want to browse without installing anything, check
out the [PDF version](https://tldr.sh/assets/tldr-book.pdf).

There are also **various other clients** provided by the community,
both for the command-line and for other platforms.
For a comprehensive list of clients, head over to our [Wiki](https://github.com/tldr-pages/tldr/wiki/tldr-pages-clients).

## How do I contribute?

- Your favourite command isn't covered?
- You can think of more examples for an existing command?

All `tldr` pages are kept as Markdown files right here in this repository,
so you can edit them directly and submit your changes as pull requests.

All contributions are welcome!
We strive to maintain a [welcoming and collaborative](GOVERNANCE.md) community.
Have a look at the [contributing guidelines](CONTRIBUTING.md), and go ahead!

If you'd like to contribute to translations, you can visit <https://lukwebsforge.github.io/tldri18n/>
to see the current progress of all translations.

## Similar projects

- [Bro pages](http://bropages.org/)
  are a highly readable supplement to man pages.
  Bro pages show concise, common-case examples for Unix commands.
  The examples are submitted by the user base, and can be voted up or down;
  the best entries are what people see first when they look up a command.

- [Cheat](https://github.com/cheat/cheat)
  allows you to create and view interactive cheatsheets on the command-line.
  It was designed to help remind *nix system administrators of options
  for commands that they use frequently, but not frequently enough to remember.

- [cheat.sh](https://cheat.sh/)
  Aggregates cheat sheets from multiple sources (including tldr-pages)
  into 1 unified interface.

- [devhints](https://devhints.io/)
  Rico's cheatsheets are not just focused on the command-line and
  include a plethora of other cheatsheets related to programming.

- [eg](https://github.com/srsudar/eg)
  provides detailed examples with explanations on the command-line.
  Examples come from the repository, but `eg` supports displaying
  custom examples and commands alongside the defaults.
  
- [kb](https://github.com/gnebbia/kb)
  is a minimalist command-line knowledge base manager.
  kb can be used to organize your notes and cheatsheets in a minimalist
  and clean way. It also supports non-text files.

- [navi](https://github.com/denisidoro/navi)
  is an interactive cheatsheet tool, which allows you to browse through
  specific examples or complete commands on the fly.

## What does "tldr" mean?

TL;DR stands for "Too Long; Didn't Read".
It originated as Internet slang, where it is used to indicate that a long text
(or parts of it) has been skipped as too lengthy.
Read more in How-To Geek's [article](https://www.howtogeek.com/435266/what-does-tldr-mean-and-how-do-you-use-it/).
