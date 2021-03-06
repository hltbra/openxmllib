==========
openxmllib
==========

openxmllib is a set of tools that deals with the new ECMA 376 office
file formats known as OpenXML.

http://www.ecma-international.org/publications/standards/Ecma-376.htm

OpenXML format is actually used by Microsoft Office 2007. Apple
iWork'08 and OpenOffice 2.2 have filters to use this format too.

Features
==========

Tested features
---------------

* Extract words from a document for indexing purpose.
* Get metadata from a document
* Get metadata from a document via URL (like http://www.foo.com/doc.docx)

Planned features
----------------

* Transform a document to HTML

Public API
==========

  >>> import openxmllib
  >>> doc = openxmllib.openXmlDocument('office.docx')
  >>> # Raises a ValueError on not supported office files.
  >>> doc.mimeType
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
  >>> doc.coreProperties # Keys may depend on application
  {'title': u'blah...', u'creator': u'John Doe', ...}
  >>> doc.extendedProperties # Keys may depend on application
  {'Words': u'312', 'Application': u'Your favorite word processor', ...}
  >>> doc.customProperties # May return an empty mapping
  {'My property': u'My value', ...}
  >>> doc.allProperties # Merges core+extended+custom properties (see above)
  {...}
  >>> doc.indexableText(include_properties=False)
  u'all the words of that document body'
  >>> doc.indexableText(include_properties=True)
  u'all the words of that document body and all properties values'

Note that if you're not running a Python application, you may get the indexable
text from a document with the `openxmlinfo.py` console utility. Just type::

  $ openxmlinfo.py --help

Copying and License
===================

Copyright (c) 2008 Gilles Lenfant

This software is subject to the provisions of the GNU General Public
License, Version 2.0 (GPL).  A copy of the GPL should accompany this
distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY,
AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE

More details in the ``COPYING`` file included in this package.

Status
======

This software is in production quality, has been tested on Mac OSX, Linux and
Windows with Python 2.4, Python 2.5, lxml 1.3.6 and lxml 2.2.

It should work on other platforms, with Python 2.6, perhaps with
other versions of lxml.

Installation
============

$ [sudo] easy_install openxmllib

Note that this will install the excellent `lxml` egg too if not already done.

From now you can "import openxmllib" in your Python apps and use the
"openxmlinfo.py" command line utility.

Gotchas
=======

Be aware that most text data coming from the various openxmllib
services might be us-ascii or Unicode. This is a side effect of lxml
(bug or feature ?). It's up to your application to convert these texts
to the appropriate charset.

We do not actually handle exceptions due to malformed XML or various
unexpected structures. You should handle the various (potential)
problems in a try (...) except (...) block in your application.

Developing and testing
======================

You should grab openxmllib with Git from Hugo's fork at `GitHub <http://github.com/hugobr/openxmllib>`_.

Then::

  $ cd /where/you/installed/openxmllib
  $ python setup.py develop

Note that testing does not require the installation::

  $ cd tests
  $ python runalltests.py

Credits
=======

Gilles Lenfant <gilles dot lenfant at gmail dot com>
Hugo Lopes Tavares <hltbra at gmail dot com>
