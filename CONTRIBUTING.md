# Contributing

[![Gitter chat][gitter-image]][gitter-url]
[![Merged PRs][prs-merged-image]][prs-merged-url]
[![Issue stats][issuestats-image]][issuestats-url]
[![GitHub contributors][contributors-image]][contributors-url]
[![CLA assistant][cla-assistant-image]][cla-assistant-url]
[![license][license-image]][license-url]

[gitter-url]: https://gitter.im/tldr-pages/tldr
[gitter-image]: https://badges.gitter.im/tldr-pages/tldr.svg
[prs-merged-url]: https://github.com/tldr-pages/tldr/pulls?q=is:pr+is:merged
[prs-merged-image]: https://img.shields.io/github/issues-pr-closed-raw/tldr-pages/tldr.svg?label=merged+PRs
[issuestats-url]: http://isitmaintained.com/project/tldr-pages/tldr
[issuestats-image]: http://isitmaintained.com/badge/resolution/tldr-pages/tldr.svg
[contributors-url]: https://github.com/tldr-pages/tldr/graphs/contributors
[contributors-image]: https://img.shields.io/github/contributors/tldr-pages/tldr.svg
[cla-assistant-url]: https://cla-assistant.io/tldr-pages/tldr
[cla-assistant-image]: https://cla-assistant.io/readme/badge/tldr-pages/tldr
[license-url]: https://github.com/tldr-pages/tldr/blob/master/LICENSE.md
[license-image]: https://img.shields.io/github/license/tldr-pages/tldr.svg

Contributions to the tldr-pages project are [most welcome](GOVERNANCE.md)!
All `tldr` pages are stored in Markdown right here on GitHub.
Just open an issue or send a pull request and we'll incorporate it as soon as possible.
To get started, please [sign](https://cla-assistant.io/tldr-pages/tldr) the
[Contributor License Agreement](https://gist.github.com/waldyrious/e50feec13683e565769fbd58ce503d4e).

*Note*: when submitting a new command, don't forget to check if there's already a pull request in progress for it.

## Guidelines

The basic format of a `tldr` page is a set of concrete usage examples.
Here are a few guidelines to get started:

1. Try to keep pages at around 5 examples. Pages can be longer if needed, but don't exceed 8 examples.
   Remember, it's OK if the page doesn't cover everything; that's what `man` is for.
2. When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
   For example, commands that require `sudo` should include it directly in the examples.
3. Try to incorporate the spelled-out version of single-letter options in the example's description.
   The goal is to allow people to *understand* the syntax of the commands, not just *memorize* it.
4. Introduce options gradually, starting with the simplest command invocations,
   and using more complex examples progressively.
5. Focus on details specific to the command, and avoid explaining general UNIX concepts that could apply to any command
   (ex: relative/absolute paths, glob patterns/wildcards, special character escaping...).

These are all guidelines, not strict rules.
Use proper judgement, keeping simplicity and user-friendliness as the top priority.

When in doubt, have a look at a few existing pages :).

## Markdown format

As a quick reference, the format of each page should match the following template:

```
# command-name

> Short, snappy description.
> Preferably one line; two are acceptable if necessary.

- Example description:

`command -opt1 -opt2 -arg1 {{arg_value}}`

- Example description:

`command -opt1 -opt2`
```

For more detailed page formatting guidelines,
refer to the [style guide](contributing-guides/style-guide.md).

## Translations

Translation of pages can be done by simply creating the corresponding page in the appropriate top level language specific directory under the appropriate platform subdirectory.
When translating a page into a language that is not present yet, a new language specific directory must be created first.

Language specific directories must follow the pattern `pages.<language_tag>`, where `<language_tag>` is a [BCP 47](https://tools.ietf.org/html/bcp47) conforming tag in the form `<language>-<region>`, where:

 - `<language>` is the shortest [ISO 639](https://en.wikipedia.org/wiki/ISO_639) language code for the chosen language (see [here](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) for a complete list).
 - `<region>` is the two-letter [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) region code for the chosen region (see [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for a complete list).

Some examples:

 - English (United Kingdom): `pages.en-GB`.
 - Chinese (Taiwan): `pages.zh-TW`.
 - Portuguese (Brazil): `pages.pt-BR`.

You can check the validity of BCP 47 tags [here](http://schneegans.de/lv/).

### Default language for newly added pages

The default language used for pages is English (US). Pages written in English are stored in the default `pages` directory (notice the absence of a specific language tag). Translations should be added only for pages that already exist in the default language. If you'd like to add a new page in a different language, please consider creating the English page first.

### Different regions for the same language

For the same language, if there virtually is no difference in writing between the country of origin and another country in which the language is spoken, then the former should always be preferred. In such cases, please choose the region code of the country of origin, to avoid fragmentation of pages for the same language. As an example, both `fr-FR` and `fr-BE` should fall under the same `pages.fr-FR` directory, since there virtually is no difference in written French between France (country of origin) and Belgium. The same goes for `en-US`, `en-GB`, `en-CA` (and so on), which should all fall under the default `pages` directory.

## Submitting a pull request

The easiest way to submit a change is to just edit the page directly on the Github interface.
Check out the step-by-step instructions (with screenshots) on
[Github Help](https://help.github.com/articles/editing-files-in-another-user-s-repository/).

Alternatively, you can do most of the process
[using git on the command line](contributing-guides/git-terminal.md).

### Commit message

For the commit message, use the following format:

    <command>: type of change

Examples:
  - For a new page addition: `ls: add page`
  - For a page edit: `cat: fix typo`, `git-push: add --force example`
  - For a new translation of an existing page: `cp: add Tamil translation`
  - For related changes to several pages: `grep, find, locate: synchronize format of wildcards`

## Licensing

`tldr` is licensed under the [MIT license](https://github.com/tldr-pages/tldr/blob/master/LICENSE.md).

Any contributions to this project are governed by the
[Contributor License Agreement](https://cla-assistant.io/tldr-pages/tldr).
