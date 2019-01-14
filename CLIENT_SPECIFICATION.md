# tldr-pages client specification

 - **Current Specification Version:** 2.0

This document contains the official specification for tldr-pages clients. It is _not_ a specification of the format of the pages themselves - only a specification of how a user should be able to interface with an official client. 

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## Changelog
 - v1.0 (18th December 2018)
	 - Initial draft
 - v1.1 (18th December 2018)
	 - Refined bullet points according to comments
	 - Ensure the spec specifies the _interface_, not the workings
 - v2.0 (12th January 2019)
	 - Expanded notes into full sentences


## Terminology
In order to aid the understanding of this specification document, a number of terms will be defined in this section.

### Page
tldr-pages consists of multiple _pages_ - each of which describes a specific command.

### Platform
Pages are grouped by platform. A platform is an operating system. For example, `windows`, `linux`, `osx`. The special platform `common` contains pages for commands that work identically across all platforms.


## Command-Line Interface
This section describes the standardised command-line interface (CLI) for clients implementing one. Clients that do not provide a CLI can ignore this section.

### Arguments
A number of arguments MUST be supported (unless otherwise specified if a CLI is implemented:

Argument		        | Meaning
------------------------|--------------------
`--update`				| Updates the offline cache of pages. MUST NOT be implemented if cache is not supported.
`--version`, `-v`		| Shows the current version of the client, and the version of this specification that it implements.
`--list-all`, `-a`		| Lists all the pages in the current platform to the standard output. One page name per line. Additional decoration MAY be printed to the standard error.

Clients MAY support additional custom arguments not documented here.

Here are some examples invocations using the above flags:

```bash
tldr --update
tldr --version
tldr -a
```

### Page Names
The first argument that does not start with a dash (`-`) MUST be considered the page name.

In addition, page names MAY contain spaces (e.g. `git status`) - such page names MUST be transparently concatenated with dashes (`-`). For example, the page name:

```
git checkout
```

...becomes this:

```
git-checkout
```

Here are some example invocations:

```bash
tldr 7za
tldr eyeD3
tldr git checkout
# In the below, "--foo" is a custom argument that takes a parameter.
tldr --foo bar bash
```

#### Specifying the Platform
As pages are grouped by platform, a user may want to access a platform-specific version of a page. This MUST be supported by prefixing the page name as follows:

```
windows/type
linux/sh
osx/brew
```

Example invocations are as follows:

```bash
tldr windows/type
# --foo is a custom argument, as described above
tldr --foo bar common/git merge
tldr linux/notify-send
```


## Directory Structure
This section documents the directory structure that contains the pages themselves.

The master version of every page is stored inside (but not directly) the `pages` directory. Inside this directory, there is a folder for each platform - for example `windows`, `linux`, and the special `common` platform:

 - `pages/`
	 + `common/`
	 + `linux/`
	 + `windows/`
	 + `osx/`
	 + .....etc.
	 
Additional platforms MAY be added in the future. Clients MAY NOT support new platforms (though such support is RECOMMENDED), but MUST NOT break if additional platforms are added.
	 
The pages themselves sit inside the appropriate platform folder, with the extension `.md`. Here are some example mappings:

Command name	|  Mapped name		| Filename
----------------|-------------------|-------------------
`7za`			| `7za`				| `7za.md`
`git checkout`	| `git-checkout`	| `git-checkout.md`
`tar`			| `tar`				| `tar.md`


### Translations
Other directories sit alongside the main `pages` directory, and contain translations of the master versions of every page - though pages MAY NOT have a translation available for a given language yet. Furthermore, a given language MAY NOT have a folder yet either. The format of these directories is `pages.{language-tag}`, where `{language-tag}` is a [BCP 47](https://tools.ietf.org/html/bcp47) conforming tag  in the form of `<language>-<region>`, where:

 - `<language>` is the shortest [ISO 639](https://en.wikipedia.org/wiki/ISO_639) language code for the chosen language (see [here](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) for a complete list).
 - `<region>` is the two-letter [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) region code for the chosen region (see [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for a complete list).

Some examples:

 - Chinese (Taiwan): `pages.zh-TW`.
 - Portuguese (Brazil): `pages.pt-BR`.
 - German (Germany): `pages.de-DE`.

You can check the validity of BCP 47 tags [here](http://schneegans.de/lv/).

The structure inside these translation folders is identical to that of the main `pages` folder.

**Note to self: A portion of this section is from [PR #2703](https://github.com/tldr-pages/tldr/pull/2703).**


## Page Structure
Although this specification is about the interface that clients must provide, it is also worth noting that pages are written in standard [CommonMark](https://commonmark.org/), which the exception of the non-standard `{{` and `}}` syntax, which surrounds values in an example that users may edit. Clients MUST NOT break if the page format is changed within the _CommonMark_ specification.


## Page Resolution
This section defines the algorithm by which a client can decide which page a user has requested.

After transparently replacing spaces (` `) with dashes (`-`), clients have several decisions to make:

 - The language of a page to display to a client
 - The platform to display a page from
 
### Platform
Clients MUST default to displaying tldr-page from the platform upon which the client is running. For example, a client running on _Windows 10_ will default to displaying pages from the `windows` platform. Clients MAY provide a user-configurable option to override this behaviour, however.

If a page is not available for the host platform, clients MUST fallback to the special `common` platform.

If a page is not available for either the host platform or the `common` platform, then clients SHOULD search other platforms and display a page from there - along with a warning message.

For example, a user has a client on windows, and requests the `apt` page. The client consults the platforms in the following order:

1. `windows` - Not available
2. `common` - Not available
3. `osx` - Not available
4. `linux` - Page found

Steps #3 and #4 may be done in either order.

#### If a page isn't found
If a page cannot be found in _any_ platform, then it is RECOMMENDED that clients display an error message with a link to create a new issue against the `tldr-pages/tldr` GitHub repository. Said link might take the following form:

```url
https://github.com/tldr-pages/tldr/issues/new?title=page%20request:%20{command_name}
```

....where `{command_name}` is the name of the command that was not found.

#### If multiple versions of a page were found
If multiple versions of a page were found for different platforms, then a client MAY choose to display a notice to the user notifying them of this.

## Language
Pages can be written in multiple languages. If a client has access to environment variables, several standard ones exist to specify the language in which a client should operate. If not, then clients MUST make reasonable assumptions based on the information provided by the environment in which they operate (e.g. consulting `navigator.languages` in a browser, etc.).

The [`LANG` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html) MUST be used to determine both the language of a page to display, and the display language of any interface text shown to the user (e.g. things like `Cache updated successfully`, for example).

Additionally, the [`LC_MESSAGES` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html) MAY be present. If specified, clients MUST use it's value to determine the language in which interface text is shown in (separately from the language to display the page in).

Finally, the [`LANGUAGE` environment variable](https://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html) specifies a priority list of languages that a user wishes to read in. If present, a client MUST use the defined priority list to decide on the language that to display in.

If a page is not available in the user's preferred language, then a client MUST respect the user's priority list defined in the `LANGUAGE` variable (if specified), and MAY choose to notify the user that a page in their chosen language couldn't be found (perhaps along with a link to the [translations section of the contributing guide](https://github.com/tldr-pages/tldr/blob/master/CONTRIBUTING.md#translations)).

## Other Considerations
This section contains a number of other items that don't neatly fit into any of the sections defined above.

If appropriate, it is RECOMMENDED that clients implement a cache of pages. If implemented, clients MUST download the _entire_ archive from **UNKNOWN_LOCATION**.

Additionally, clients MAY automatically update the cache on a regular basis.
