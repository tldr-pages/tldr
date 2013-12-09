var should = require('should');
var output = require('../lib/output');

describe('Console output from Markdown', function() {
  
  it('strips paragraph tags', function() {
    var o = output.fromMarkdown(
      '\nline 1' +
      '\n' +
      '\nline 2' +
      '\n'
    );
    o.should.eql('line 1line 2');
  });

  it('command description is in a block quote', function() {
    var o = output.fromMarkdown(
      '\n> archiving utility' +
      '\n> supports optional compression'
    );
    o.should.include('archiving utility');
    o.should.include('supports optional compression');
    o.should.startWith('\n  \u001b[3m\u001b[1m');
    o.should.endWith('\u001b[22m\u001b[23m\n\n');
  });
  
  it('surrounds the command description with line breaks', function() {
    var o = output.fromMarkdown(
      '\n> archiving utility' +
      '\n> supports optional compression'
    );
    o.should.endWith('\n\n');
  });
  
  it('ignores all other Markdown syntax', function() {
    var o = output.fromMarkdown(
      '\n# heading 1' +
      '\n' +
      '\n## heading 2' +
      '\n' +
      '\n[link](http://link)' +
      '\n' +
      '\n```' +
      '\ncode block' +
      '\n```'
    );
    o.should.eql('');
  });
  
});
