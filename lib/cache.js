var _         = require('lodash');
var fs        = require('fs');
var path      = require('path');
var async     = require('async');
var mkdirp    = require('mkdirp');
var rmdir     = require('rimraf');
var config    = require('./config');
var request   = require('./request');

exports.get = function(filename, done) {
  var filepath = path.join(config.local.cacheFolder, filename);
  async.waterfall([
    function(next) { checkCache(filepath, next); },
    function(next) { getContent(filepath, next); }
  ], done);
};

exports.save = function(filename, contents, done) {
  var filepath = path.join(config.local.cacheFolder, filename);
  var dir = path.dirname(filepath);
  mkdirp(dir, function(err) {
    fs.writeFile(filepath, contents, done);
  });
};

exports.clear = function() {
  rmdir(config.local.cacheFolder, function(err) {
    console.log('Cache cleared');
  });
};

exports.update = function(opts) {
  if (!opts.hasOwnProperty("branch")) {
    request.getTags(opts, function(err, tags) {
      var tag = opts.tag ? _.find(tags, {name: opts.tag}) : tags[0]; // this is super cool :D
      console.log("Updating from " + config.updateRepo + ":" + tag.name);
      request.getZip(tag.zipball_url, opts, function(err, pth) {
        if (err) {
          console.log("Error unzipping %j: %j", tag.zipball_url, err);
        } else {
          mergeRepo(pth);
        }
      });
    });
  } else {
    var branch = opts.branch ? opts.branch : "master",
        aurl = 'https://api.github.com/repos/' + config.updateRepo + '/zipball/' + branch;
    request.getZip(aurl, opts, function(err, pth) {
        if (err) {
          console.log("Error unzipping %j", aurl);
        } else {
          mergeRepo(pth);
        }
    });
  }
}

function checkCache(filepath, done) {
  fs.stat(filepath, function(err, stat) {
    if (err) {
      done("'" + path.basename(filepath).replace(/\..*\.md$/,"") + "' not found. Try updating from the server with the --update flag, or contributing a pull request to https://github.com/rprieto/tldr");
    } else {
      done(null);
    }
  });
}

function getContent(filepath, done) {
  fs.readFile(filepath, function (err, contents) {
    if (err) {
      done(path.basename(filepath) + " not found. Try updating from the server with the --update flag, or contributing Pull Request to https://github.com/rprieto/tldr");
    } else {
      done(null, contents.toString());
    }
  });
}

function copyFile(source, target, cb) {
  var cbCalled = false,
    rd = fs.createReadStream(source),
    wr = fs.createWriteStream(target);
  rd.on("error", function(err) {
    done(err);
  });
  wr.on("error", function(err) {
    done(err);
  });
  wr.on("close", function(ex) {
    done();
  });
  rd.pipe(wr);

  var done = function(err) {
    if (!cbCalled) {
      cb(err);
      cbCalled = true;
    }
  };
}

// TODO: add override flags and don't simply copy over files here unless that flag is set
function mergeRepo(pth) {
  var subdirs = fs.readdirSync(pth).filter(function(subdir) {
    var stat = fs.statSync(path.resolve(pth, subdir));
    return stat.isDirectory();
  });
  if (!fs.existsSync(config.local.cacheFolder)) {
    fs.mkdirSync(config.local.cacheFolder);
  }
  var pagesDir = path.resolve(pth, subdirs[0], "pages"),
      pagesSubdirs = fs.readdirSync(pagesDir);

  pagesSubdirs.forEach(function(dir) {
    var dpath = path.resolve(pagesDir, dir),
        pages = fs.readdirSync(dpath);
    pages.forEach(function(page) {
      if (path.extname(page) === ".md") {
        var ppath = path.resolve(dpath, page),
            npath = path.resolve(config.local.cacheFolder, path.basename(page).replace(/\.md$/,"") + "." + dir + ".md");
        if (fs.existsSync(npath)) {
          fs.unlinkSync(npath);
        }
        function nicepath(p) {
          return path.basename(path.dirname(p)) + '/' + path.basename(p);
        }
        console.log("Copying " + nicepath(ppath) + " to " + npath);
        copyFile(ppath, npath, function(err) {
          if (err) {
            console.log("ERR: " + err);
          }
        });
      }
    });
  });
}

