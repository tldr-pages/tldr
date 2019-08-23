tldr-pages client specification
===============================

**Current Specification Version:** 1.2

This document contains the official specification for tldr-pages clients. It is _not_ a specification of the format of the pages themselves - only a specification of how a user should be able to interface with an official client. For a list of previous versions of the specification, see the [changelog section](#Changelog) below.

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


Terminology
-----------

In order to aid the understanding of this specification document, a number of terms will be defined in this section.

### Page

tldr-pages consists of multiple _pages_ - each of which describes a specific command.

### Platform

Pages are grouped by platform. A platform is an operating system. For example, `windows`, `linux`, `osx`. The special platform `common` contains pages for commands that work identically across more than 1 platform.

If a page is common across multiple platforms, but slightly differently on a given platform, then the page is still stored in `common`, but a copy tailored for the differing platform is placed in that platform's specific folder.

For example, if the command `foo` is common to `mac`, `windows`, and `linux` but functions differently on `windows`, then the main page will be stored in `common`, and a copy will be placed in `windows` that's altered to match the different functionality.


Command-Line Interface
----------------------

This section describes the standardised command-line interface (CLI) for clients implementing one. Clients that do not provide a CLI can ignore this section.

### Arguments

A number of command-line options MUST be supported (unless otherwise specified) if a CLI is implemented:

Option             | Required?   | Meaning
-------------------|-------------|----------
`-v`, `--version`  | Yes         | Shows the current version of the client, and the version of this specification that it implements.
`-p`, `--platform` | Yes         | Specifies the platform to be used to perform the action (either listing or searching) as an argument. If this option is specified, the selected platform MUST be checked first instead of the current platform as described below.
`-u`, `--update`   | Conditional | Updates the offline cache of pages. MUST be implemented if cache is supported.
`-l`, `--list`     | No          | Lists all the pages in the current platform to the standard output. If the special platform `all` is specified a list of all pages in all platforms MUST be displayed.
`-L`, `--language` | No          | Specifies the preferred language for the page returned. Overrides other language detection mechanisms. See the [language section](#language) for more information.

Clients MAY choose to only implement the short version of an option, ignoring the long form.

Additional decoration MAY be printed if the standard output is a [TTY](http://www.linusakesson.net/programming/tty/index.php). If not, then the output MUST not contain any additional decorations. For example a page list MUST be formatted with 1 page name per line (to enable easy manipulation using standard CLI tools such as `grep` etc.).

Clients MAY support additional custom arguments and syntax not documented here.

Here are some examples invocations using the above flags:

```bash
tldr --update
tldr --version
tldr -l
```

### Page Names

The first argument that does not start with a dash (`-`), MUST be considered the page name.

In addition, page names MAY contain spaces (e.g. `git status`) - such page names MUST be transparently concatenated with dashes (`-`). For example, the page name:

```
git checkout
```

becomes this:

```
git-checkout
```

Here are some example invocations:

```bash
tldr 7za
tldr eyeD3
tldr git checkout
tldr --platform osx bash
```


Directory Structure
-------------------

This section documents the directory structure that contains the pages themselves.

The master version of every page is stored inside (but not directly) the `pages` directory. Inside this directory, there is a folder for each platform - for example `windows`, `linux`, and the special `common` platform:

 - `pages/`
   - `common/`
   - `linux/`
   - `windows/`
   - `osx/`
   - ...etc.

Additional platforms MAY be added in the future. Clients MAY NOT support new platforms (though such support is RECOMMENDED), but MUST NOT break if additional platforms are added.

The pages themselves reside inside the appropriate platform folder, with the extension `.md`. Here are some example mappings:

Command name    | Mapped name     | Filename
----------------|-----------------|-------------------
`7za`           | `7za`           | `7za.md`
`git checkout`  | `git-checkout`  | `git-checkout.md`
`tar`           | `tar`           | `tar.md`


### Translations

Other directories sit alongside the main `pages` directory, and contain translations of the master versions of every page - though pages MAY NOT have a translation available for a given language yet. Furthermore, a given language MAY NOT have a folder yet either. The format of these directories is `pages.<locale>`, where `<locale>` is a [POSIX Locale Name](https://www.gnu.org/software/gettext/manual/html_node/Locale-Names.html#Locale-Names) in the form of `<language>_<country>`, where:

 - `<language>` is the shortest [ISO 639](https://en.wikipedia.org/wiki/ISO_639) language code for the chosen language (see [here](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) for a complete list).
 - `<country>` is the two-letter [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code for the chosen region (see [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for a complete list).

Some examples:

 - Chinese (Taiwan): `pages.zh_TW`.
 - Portuguese (Brazil): `pages.pt_BR`.
 - Italian: `pages.it`.

The structure inside these translation folders is identical to that of the main `pages` folder.


Page Structure
--------------

Although this specification is about the interface that clients must provide, it is also worth noting that pages are written in standard [CommonMark](https://commonmark.org/), which the exception of the non-standard `{{` and `}}` syntax, which surrounds values in an example that users may edit. Clients MUST NOT break if the page format is changed within the _CommonMark_ specification.


Page Resolution
---------------

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

It is possible that due to this page resolution logic, the client may show a page which does not belong to the host platform because a page can reside in `common`, and not be present on the host platform. Clients must not assume that a given command is always executable on the host platform.

#### If a page is not found

If a page cannot be found in _any_ platform, then it is RECOMMENDED that clients display an error message with a link to create a new issue against the `tldr-pages/tldr` GitHub repository. Said link might take the following form:

```url
https://github.com/tldr-pages/tldr/issues/new?title=page%20request:%20{command_name}
```

where `{command_name}` is the name of the command that was not found.

#### If multiple versions of a page were found

If multiple versions of a page were found for different platforms, then a client MAY choose to display a notice to the user notifying them of this.


Language
--------

Pages can be written in multiple languages. If a client has access to environment variables, several standard ones exist to specify the language in which a client should operate. If not, then clients MUST make reasonable assumptions based on the information provided by the environment in which they operate (e.g. consulting `navigator.languages` in a browser, etc.). If possible, it is RECOMMENDED to also make language configurable, as to not only rely on the environment. Clients SHOULD therefore offer options to configure or override the language using configuration files or command line options (like `-L, --language` as suggested in the [options section](#Options) above).

The [`LANG` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html), if present, MUST be used to determine the language of pages to display.

The [`LANGUAGE` environment variable](https://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html) specifies a priority list of languages that a user wishes to read in. In absence of `LANG` and if this environment variable present, a client MUST use the defined priority list to decide on the language of pages to display. If a page is not available in the user's preferred language, then a client MUST respect the user's priority list defined in the `LANGUAGE` variable, and MAY choose to notify the user that a page in their chosen language couldn't be found (perhaps along with a link to the [translations section of the contributing guide](https://github.com/tldr-pages/tldr/blob/master/CONTRIBUTING.md#translations)).

The [`LC_MESSAGES` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html) MAY be present. If the client itself is localized and this environment variable is present, it MUST use its value in order to determine the language in which interface text is shown (separately from the language used for pages). In absence of `LC_MESSAGES`, then `LANG` and `LANGUAGE` MUST be used for this purpose instead.

**Note that** it is highly RECOMMENDED to give precedence to the platform first, and then the language. In other words, look for a platform under each language, before falling back to the next preferred language. This ensures a meaningful and correct page resolution.

Here's an example of how the lookup should be done on `linux` having set `LANGUAGE="it:fr:en"`:

    1. pages.it/linux/some-page.md  -> does not exist
    2. pages.fr/linux/some-page.md  -> does not exist
    3. pages/linux/some-page.md     -> does not exist
    4. pages.it/common/some-page.md -> does not exist
    5. pages.fr/common/some-page.md -> does not exist
    6. pages/common/some-page.md    -> FOUND!

Caching
-------

If appropriate, it is RECOMMENDED that clients implement a cache of pages. If implemented, clients MUST download the archive either from **[http://tldr.sh/assets/tldr.zip](http://tldr.sh/assets/tldr.zip)** or [https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/master/assets/tldr.zip](https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/master/assets/tldr.zip) (which is pointed by the first link).

Caching SHOULD be done according to the user's language configuration (if any), as to not waste unneeded space for unneeded languages. Additionally, clients MAY automatically update the cache on a regular basis.


Changelog
---------

 - [v1.2, July 3rd 2019](https://github.com/tldr-pages/tldr/blob/master/CLIENT-SPECIFICATION.md) (#3168)
   - Addition of a new `-L, --language` recommended command-line option.
   - Rewording of the language section also encouraging the use of configuration files for language.
   - Shift from BCP-47 to POSIX style locale tags, with consequent **deprecation of previous versions of the spec**.
   - Clearer clarification about the recommended caching functionality.
   - Correction of the usage of the term "arguments" in the homonym section.

 - [v1.1, April 1st 2019](https://github.com/tldr-pages/tldr/blob/fbdc06b7425f92cc0d4fc9a5cfc5860ef017251e/CLIENT-SPECIFICATION.md) (deprecated) (#2859)
   - Clarified platform section.

 - [v1.0, January 23rd 2019](https://github.com/tldr-pages/tldr/blob/f5be8a2614a455288f26e42953efeb8cb3bc50b0/CLIENT-SPECIFICATION.md) (deprecated) (#2706)
   - Initial release.
