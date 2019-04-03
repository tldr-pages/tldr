'use strict';

const glob = require('glob');

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
    } else {
      index[page] = {name: page, platform: [os], language: [language]};
    }

    return index;
  };

  let obj = files.reduce(reducer, {});

  return Object.keys(obj)
      .sort()
      .map(function(page) {
        return {
          name: page,
          platform: obj[page]["platform"],
          language: obj[page]["language"]
        };
      });
}

function saveIndex(index) {
  let indexFile = {
    commands: index
  };

  console.log(JSON.stringify(indexFile));
}

glob('pages*/**/*.md', function (er, files) {
  if (er !== null) {
    console.error('ERROR finding pages!');
    console.error(er);
    return;
  }

  let index = buildPagesIndex(files);
  saveIndex(index);
});
