# Style guide
### Wording

- All descriptions **must be concise**.
- Avoid using the page title in the description (e.g. use `A sketching and painting program designed for digital artists` instead of `Krita is a sketching and painting program designed for digital artists`) unless the program name differs from the executable name (e.g. `rg` and Ripgrep).
- Avoid mentioning that the program is used on the command-line (e.g. use `Ripgrep is a recursive line-oriented search tool` instead of `Ripgrep is a recursive line-oriented CLI search tool`).
- For example, when writing documentation for `cd`, a tool to change the current working directory in the Terminal or Command Prompt, **do not** write a lengthy description such as:

```md
> `cd` is a system tool, available in Windows, macOS, and Linux, to change the current working directory to get things done in the Command Prompt, Terminal, and PowerShell.
```

It should instead be simplified to make it easier for everyone to read:

```md
> Change the current working directory.
```

### Formatting

- Proper names should be capitalized in the description whenever applicable (e.g. use `A tool for interacting with a Git repository.` instead of ``A tool for interacting with a `git` repository.``).
- Acronym expansions (i.e. protocols, tools, etc) must not be translated unless there is a recognized native equivalent for them.
- When documenting keycaps or a keyboard shortcut for a utility, to make it stand out in the description:
1. If it is not translatable, enclose it with backticks (i.e. ``Print the last lines of a given file and keep reading it until `Ctrl + C`:``)
2. If it is translatable, enclose it with double angled brackets (i.e. ``:wq<<Enter>>``).

## Emphasis

Do not use *italics*, **boldface** or any other text styling on the pages. These are reserved for client emphasis of placeholders.

## Serial Comma

- When declaring a list of 3 or more items,
use a [serial comma](https://en.wikipedia.org/wiki/Serial_comma),
also known as the Oxford comma,
since omitting it can create ambiguity.

> Delete the Git branches, tags and remotes.

The example above does not use a serial comma, so this could mean one of two things:

- Delete the Git branches named `tags` and `remotes`.
- Delete all of the following: Git branches, Git tags, and Git remotes.

This can be resolved by inserting a comma before the "and" or "or" in the final element in the list.

> Delete the Git branches, tags, and remotes.

## See also section

- To reference a related command or subcommand, use:

```md
> See also: `command`.
```

- To reference related commands or subcommands, use:

```md
> See also: `command1`, `command2`, `command3`.
```

- Optionally, you can add a short description beside the referenced pages:

``See also: `date`, for Unix information; `umount`, for unmounting partitions.``

## More information links

- On the `More information` link line, we prefer linking to the author's provided documentation of the command line reference or the man page. When not available, use <https://manned.org> as the default fallback for all platforms (except `osx` and BSD platforms other than FreeBSD). Alternatively, you can link to the author's website or a tutorial page if the command doesn't have a documentation page.

- For `osx`: Apple distributes the built-in man pages [in Xcode](https://developer.apple.com/documentation/os/reading_unix_manual_pages). For commands documented there, we recommend using https://keith.github.io/xcode-man-pages/, an HTML export of all Apple's man pages bundled with Xcode.

- **All links must be enclosed inside angular brackets (`<` and `>`) for proper rendering in clients.**

- We prefer translations to use the more information link of the English page by default.

### Versioned links

When a utility or distribution has versioned links for the packages, we prefer linking to the most recent version of documentation (i.e. `latest`) or none if the website automatically redirects to the latest version of the documentation.

For example, use:

- <https://manpages.debian.org/latest/apt/apt.8.html> instead of <https://manpages.debian.org/bookworm/apt/apt.8.en.html>.
- <https://docs.aws.amazon.com/cdk/latest/guide/cli.html> instead of <https://docs.aws.amazon.com/cdk/v2/guide/cli.html>.

### Microsoft Learn links

When linking pages to the Microsoft Learn links, remove the locale from the address as the website will automatically redirect to the reader's preferred locale setting. For example, Use <https://learn.microsoft.com/windows-server/administration/windows-commands/cd> instead of
<https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd>.

Additionally, if the link is related to PowerShell command documentation, remove the **documentation version indicator** (in which the version of PowerShell/module that the documentation is derived from), aka. the part of the address that starts with `?view=`.

- Use <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string> instead of <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string?view=powershell-7.4>.
- Use <https://learn.microsoft.com/powershell/module/powershellget/install-module> instead of <https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module?view=powershellget-1.x>.

## Help and version commands

- We generally put, **in this order**, the help and version commands as the **last two** examples of the page to highlight more practical commands at the beginning of the page. They can be replaced to accommodate other useful examples if required.
- For consistency, we prefer generic wording `Display help` and `Display version` for these commands.
- It is suggested to document the help and version examples if the command follows unconventional flags in platforms like Windows.

## Language-Specific Rules

The below section contains additional language-specific rules for translating pages:

### Chinese-Specific Rules

When Chinese words, Latin words and Arabic numerals are written in the same sentence, more attention must be paid to copywriting.

The following guidelines are applied to Chinese (`zh`) and traditional Chinese (`zh_TW`) pages:
