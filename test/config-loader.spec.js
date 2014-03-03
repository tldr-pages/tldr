var fs     = require('fs');
var path   = require('path');
var sinon  = require('sinon');
var should = require('should');
var loader = require('../lib/config-loader');

describe('Config', function() {

  var DEFAULT =
    '{' +
    '  "remote": {' +
    '    "url": "http://default-pages" ' +
    '  }' +
    '}';

  var CUSTOM =
    '{' +
    '  "remote": {' +
    '    "url": "http://custom-pages" ' +
    '  }' +
    '}';

  var CUSTOM_INVALID =
    '{' +
    '  "colors": {' +
    '    "text": "pretty" ' +
    '  }' +
    '}';

  beforeEach(function() {
    sinon.stub(fs, 'readFileSync');
  });

  afterEach(function() {
    fs.readFileSync.restore();
  });

  it('should load the default config', function() {
    fs.readFileSync.onCall(0).returns(DEFAULT);
    fs.readFileSync.onCall(1).throws('Not found');
    loader.get().remote.url.should.eql('http://default-pages');
  });

  it('should override the defaults with content from .tldrrc', function() {
    fs.readFileSync.onCall(0).returns(DEFAULT);
    fs.readFileSync.onCall(1).returns(CUSTOM);
    loader.get().remote.url.should.eql('http://custom-pages');
  });

  it('should validate the custom config format', function() {
    fs.readFileSync.onCall(0).returns(DEFAULT);
    fs.readFileSync.onCall(1).returns(CUSTOM_INVALID);
    loader.get.should.throw(/Invalid ANSI color/);
  });

});
