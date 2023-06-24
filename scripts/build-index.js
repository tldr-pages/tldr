// SPDX-License-Identifier: MIT

'use strict';

const { glob } = require('glob');

function parsePlatform(pagefile) {
  return pagefile.split(/\//)[1];
}

function parsePagename(pagefile) {
  return pagefile.split(/\//)[2].replace(/\.md$/, '');
}

function parseLanguage(pagefile) {
  let pagesFolder = pagefile.split(/\//)[0];
  return pagesFolder == 'pages' ? 'en' : pagesFolder.replace(/^pages\./, '');
}

function buildPagesIndex(files) {
  let reducer = function (index, file) {
    let os = parsePlatform(file);
    let page = parsePagename(file);
    let language = parseLanguage(file);

    if (index[page]) {
      if (!index[page].platform.includes(os)) {
        index[page].platform.push(os);
      }

      if (!index[page].language.includes(language)) {
        index[page].language.push(language);
      }

      const targets = index[page].targets;
      const exists = targets.some((t) => {return t.platform === os && t.language === language});
      if (!exists) {
        targets.push({os, language})
      }
    } else {
      index[page] = {
        name: page,
        platform: [os],
        language: [language],
        targets: [{os, language}]
      };
    }

    return index;
  };

  let obj = files.reduce(reducer, {});

  return Object.keys(obj)
      .sort()
      .map(function(page) {
        return {
          name: page,
          platform: obj[page].platform,
          language: obj[page].language,
          targets: obj[page].targets
        };
      });
}

function saveIndex(index) {
  let indexFile = {
    commands: index
  };

  console.log(JSON.stringify(indexFile));
}

(async () => {
  const files = await glob('pages*/**/*.md');
  let index = buildPagesIndex(files);
  saveIndex(index);
})().then(() => {
  process.exit(0);
}).catch((err) => {
  console.error('ERROR building index!');
  console.error(er);
  process.exit(1);
});
