# -*- coding: utf-8 -*-

from blogmarks.blogmarks_parser import parser

ONE_BLOGMARK = """
<entry>
  <id>tag:blogmarks.net,2013:1058976312</id>
  <title>Films Noir et Blanc Format 120</title>
  <updated>2013-05-22T18:12:48Z</updated>
  <published>2013-05-22T18:12:48Z</published>
  <author>
    <name>jpcaruana</name>
    <uri>http://blogmarks.net/user/jpcaruana</uri>
  </author>
  <link href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm"/>
  <link rel="related" href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm" type="text/html"/>
  <link rel="edit" href="http://blogmarks.net/api/user/jpcaruana/mark/1058976312" type="application/atom+xml"/>
  <link rel="alternate" href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm" type="text/html"/>
  <link rel="avatar" href="http://blogmarks.net/avatar/3c13ffe3d0e3d8512cdd4e3f5c000d9e"/>
  <link rel="via" href="http://www.google.fr/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;ved=0CD4QFjAA&amp;url=http%3A%2F%2Fwww.photostock.fr%2Ffilms-noir-et-blanc-format-120%2Cfr%2C3%2C179.cfm&amp;ei=hAqdUdHxE_KV7AbL34CoDA&amp;usg=AFQjCNGCPkq9cInER0dTumn7YINYeelZtA&amp;sig2=VKdCY3xzYV9qH8qEuwC28Q" type="text/html"/>
  <link rel="enclosure" href="http://blogmarks.net/screenshots/2013/05/22/365950c1d5f250d8c2cce17f8cf84ab3.jpg" type="image/jpg"/>
  <category scheme="http://blogmarks.net/tag/" term="photographie" label="photographie"/>
  <category scheme="http://blogmarks.net/tag/" term="lomo" label="lomo"/>
  <activity:verb>http://activitystrea.ms/schema/1.0/post</activity:verb>
  <activity:object>
    <activity:object-type>http://activitystrea.ms/schema/1.0/bookmark</activity:object-type>
  </activity:object>
</entry>"""

ONE_BLOGMARK_WITH_COMMENT = """
<entry>
  <id>tag:blogmarks.net,2013:1058948771</id>
  <title>darktable | the photo workflow software</title>
  <updated>2013-01-23T18:40:51Z</updated>
  <published>2013-01-23T18:40:51Z</published>
  <author>
    <name>jpcaruana</name>
    <uri>http://blogmarks.net/user/jpcaruana</uri>
  </author>
  <link href="http://www.darktable.org/"/>
  <link rel="related" href="http://www.darktable.org/" type="text/html"/>
  <link rel="edit" href="http://blogmarks.net/api/user/jpcaruana/mark/1058948771" type="application/atom+xml"/>
  <link rel="alternate" href="http://www.darktable.org/" type="text/html"/>
  <link rel="avatar" href="http://blogmarks.net/avatar/3c13ffe3d0e3d8512cdd4e3f5c000d9e"/>
  <link rel="via" href="http://www.questionsphoto.com/logiciels-dimage-les-nouveautes-du-mois/" type="text/html"/>
  <link rel="enclosure" href="http://blogmarks.net/screenshots/2013/01/23/b9937f477c0780a62388a1db16e058a0.jpg" type="image/jpg"/>
  <category scheme="http://blogmarks.net/tag/" term="photographie" label="photographie"/>
  <category scheme="http://blogmarks.net/tag/" term="open%2Bsource" label="open source"/>
  <category scheme="http://blogmarks.net/tag/" term="apps" label="apps"/>
  <content type="text"><![CDATA[darktable is an open source photography workflow application and RAW developer. A virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop raw images and enhance them.]]></content>
  <activity:verb>http://activitystrea.ms/schema/1.0/post</activity:verb>
  <activity:object>
    <activity:object-type>http://activitystrea.ms/schema/1.0/bookmark</activity:object-type>
  </activity:object>
</entry>"""

ONE_BLOGMARK_WITH_PRIVATE_TAG = """
<entry>
  <id>tag:blogmarks.net,2013:1058976312</id>
  <title>Films Noir et Blanc Format 120</title>
  <updated>2013-05-22T18:12:48Z</updated>
  <published>2013-05-22T18:12:48Z</published>
  <author>
    <name>jpcaruana</name>
    <uri>http://blogmarks.net/user/jpcaruana</uri>
  </author>
  <link href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm"/>
  <link rel="related" href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm" type="text/html"/>
  <link rel="edit" href="http://blogmarks.net/api/user/jpcaruana/mark/1058976312" type="application/atom+xml"/>
  <link rel="alternate" href="http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm" type="text/html"/>
  <link rel="avatar" href="http://blogmarks.net/avatar/3c13ffe3d0e3d8512cdd4e3f5c000d9e"/>
  <link rel="via" href="http://www.google.fr/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;ved=0CD4QFjAA&amp;url=http%3A%2F%2Fwww.photostock.fr%2Ffilms-noir-et-blanc-format-120%2Cfr%2C3%2C179.cfm&amp;ei=hAqdUdHxE_KV7AbL34CoDA&amp;usg=AFQjCNGCPkq9cInER0dTumn7YINYeelZtA&amp;sig2=VKdCY3xzYV9qH8qEuwC28Q" type="text/html"/>
  <link rel="enclosure" href="http://blogmarks.net/screenshots/2013/05/22/365950c1d5f250d8c2cce17f8cf84ab3.jpg" type="image/jpg"/>
  <category scheme="http://blogmarks.net/tag/" term="photographie" label="photographie"/>
  <category scheme="http://blogmarks.net/tag/" term="lomo" label="lomo"/>
  <category scheme="http://blogmarks.net/user/jpcaruana/private-tag/" term="this_is_private" label="this_is_private"/>
  <activity:verb>http://activitystrea.ms/schema/1.0/post</activity:verb>
  <activity:object>
    <activity:object-type>http://activitystrea.ms/schema/1.0/bookmark</activity:object-type>
  </activity:object>
</entry>"""

FULL_IMPORT_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>

<feed xmlns="http://www.w3.org/2005/Atom" xmlns:bm="http://blogmarks.net/ns/" xmlns:openSearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:app="http://www.w3.org/2007/app" xmlns:activity="http://activitystrea.ms/spec/1.0/" >

  <id>bm-marks-users:10091-includePrivates:1,10091-last:100000</id>
  <title>Mes marks</title>
  <updated>2014-02-20T16:31:57Z</updated>

  <openSearch:totalResults>2042</openSearch:totalResults>
  <openSearch:startIndex>0</openSearch:startIndex>
  <openSearch:itemsPerPage>100000</openSearch:itemsPerPage>

  <link rel="self" type="application/atom+xml" href="http://blogmarks.net/api/user/jpcaruana/marks/?last=100000&amp;includePrivates=1&amp;format=atom" title="Mes marks"/>
  <link rel="alternate" type="text/html" href="http://blogmarks.net/my/marks/?last=100000&amp;includePrivates=1" title="Mes marks"/>

{entry}

</feed>"""


def test_parse_one_mark():
    entries = parser(FULL_IMPORT_TEMPLATE.format(entry=ONE_BLOGMARK))

    entry = next(entries)
    assert entry.entry_id == '1058976312'
    assert entry.url == "http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm"
    assert entry.title == "Films Noir et Blanc Format 120"
    assert entry.tags == ['photographie', 'lomo']
    # assert entry.date == datetime.datetime(2013, 5, 22, 18, 12, 48)


def test_do_not_parse_private_tags():
    entries = parser(FULL_IMPORT_TEMPLATE.format(entry=ONE_BLOGMARK_WITH_PRIVATE_TAG))

    entry = next(entries)
    assert entry.entry_id == '1058976312'
    assert entry.url == "http://www.photostock.fr/films-noir-et-blanc-format-120,fr,3,179.cfm"
    assert entry.title == "Films Noir et Blanc Format 120"
    assert entry.tags == ['photographie', 'lomo']


def test_parse_comment():
    entries = parser(FULL_IMPORT_TEMPLATE.format(entry=ONE_BLOGMARK_WITH_COMMENT))

    entry = next(entries)
    assert entry.entry_id == '1058948771'
    assert entry.url == "http://www.darktable.org/"
    assert entry.title == "darktable | the photo workflow software"
    assert entry.tags == ['photographie', "open source", 'apps']
    assert entry.comment == 'darktable is an open source photography workflow application and RAW developer. ' \
                            'A virtual lighttable and darkroom for photographers. It manages your digital negatives' \
                            ' in a database, lets you view them through a zoomable lighttable and enables you to ' \
                            'develop raw images and enhance them.'
