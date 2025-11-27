// SPDX-License-Identifier: MIT

'use strict';

const { glob } = require('glob');
const { sep } = require('path');

/**
 * Parse the OS/platform from a page file path.
 */
function parsePlatform(pagefile) {
  return pagefile.split(sep)[1];
}

/**
 * Parse the page name from a page file path.
 */
function parsePagename(pagefile) {
  return pagefile.split(sep)[2].replace(/\.md$/, '');
}

/**
 * Determine the language of the page.
 */
function parseLanguage(pagefile) {
  const pagesFolder = pagefile.split(sep)[0];
  return pagesFolder === 'pages' ? 'en' : pagesFolder.replace(/^pages\./, '');
}

/**
 * Build an index of all pages with their platforms and languages.
 */
function buildPagesIndex(files) {
  const reducer = (index, file) => {
    const os = parsePlatform(file);
    const page = parsePagename(file);
    const language = parseLanguage(file);

    if (!index[page]) {
      index[page] = {
        name: page,
        platform: [os],
        language: [language],
        targets: [{ os, language }],
      };
    } else {
      if (!index[page].platform.includes(os)) {
        index[page].platform.push(os);
      }

      if (!index[page].language.includes(language)) {
        index[page].language.push(language);
      }

      const exists = index[page].targets.some(
        (t) => t.os === os && t.language === language
      );
      if (!exists) {
        index[page].targets.push({ os, language });
      }
    }

    return index;
  };

  const obj = files.reduce(reducer, {});

  return Object.keys(obj)
    .sort()
    .map((page) => ({
      name: page,
      platform: obj[page].platform,
      language: obj[page].language,
      targets: obj[page].targets,
    }));
}

/**
 * Output the final index JSON.
 */
function saveIndex(index) {
  const indexFile = { commands: index };
  console.log(JSON.stringify(indexFile, null, 2));
}

// Main execution
(async () => {
  try {
    const files = await glob('pages*/**/*.md');
    const index = buildPagesIndex(files);
    saveIndex(index);
    process.exit(0);
  } catch (err) {
    console.error('ERROR building index!');
    console.error(err);
    process.exit(1);
  }
})();
