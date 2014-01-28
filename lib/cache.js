var fs     = require('fs');
var path   = require('path');
var async  = require('async');
var mkdirp = require('mkdirp');
var config = require('./config');

exports.get = function(filename, done) {
  var filepath = path.join(config.local.cacheFolder, filename);
  async.waterfall([
    function(next) { checkCache(filepath, next); },
    function(next) { getContent(filepath, next); }
  ], done);
};

exports.save = function(filename, contents, done) {
  mkdirp(config.local.cacheFolder, function(err) {
    var filepath = path.join(config.local.cacheFolder, filename);
    fs.writeFile(filepath, contents, done);
  });
};

function checkCache(filepath, done) {
  fs.stat(filepath, function(err, stat) {
    if (err) {
      done('cache miss: ' + filepath);
    } else {
      var age = (new Date().getTime() - stat.mtime.getTime()) / 1000;
      if (age > config.remote.maxAge) {
        done('cache too old:' + filepath);
      } else {
        done(null);
      }
    }
  });
}

function getContent(filepath, done) {
  fs.readFile(filepath, function (err, contents) {
    if (err) {
      done('cache miss: ' + filepath);
    } else {
      done(null, contents.toString());
    }
  });
}
