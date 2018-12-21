'use strict';

var glob = require('glob');

function parsePlatform(pagefile) {
  return pagefile.split(/\//)[1];
}

function parsePagename(pagefile) {
  return pagefile.split(/\//)[2].replace(/\.md$/, '');
}

function parseLanguage(pagefile) {
  var pagesFolder = pagefile.split(/\//)[0];
  return pagesFolder == 'pages' ? 'en' : pagesFolder.replace(/^pages./, '');
}

function buildPagesIndex(files) {
  var reducer = function (index, file) {
    var os = parsePlatform(file);
    var page = parsePagename(file);
    var language = parseLanguage(file);
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

  var obj = files.reduce(reducer, {});
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
  var indexFile = {
    commands: index
  };
  console.log(JSON.stringify(indexFile));
}

glob('pages*/**/*.md', function (er, files) {
  var index = buildPagesIndex(files);
  saveIndex(index);
});
