'use strict';

var glob = require('glob');

function parsePlatform(pagefile) {
  return pagefile.split(/\//)[1];
}

function parsePagename(pagefile) {
  return pagefile.split(/\//)[2].replace(/\.md$/, '');
}

function buildShortPagesIndex(files) {
  var reducer = function (index, file) {
    var os = parsePlatform(file);
    var page = parsePagename(file);
    if (index[page]) {
      index[page].push(os);
    } else {
      index[page] = [os];
    }
    return index;
  };

  return files.reduce(reducer, {});
}

function buildPagesIndex(shortIndex) {
  return Object.keys(shortIndex)
    .sort()
    .map(function (page) {
      return {
        name: page,
        platform: shortIndex[page]
      };
    });
}

function saveIndex(index) {
  var indexFile = {
    commands: index
  };
  console.log(JSON.stringify(indexFile));
}

glob('pages/**/*.md', function (er, files) {
  var shortIndex = buildShortPagesIndex(files);
  var index = buildPagesIndex(shortIndex);
  saveIndex(index);
});
