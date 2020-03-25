# -*- coding: utf-8 -*-
from blogmarks.blogmarks_parser import Bookmark
from blogmarks.hugo_bookmark_formater import formater
from datetime import datetime


def test_with_title():
    bookmark_dict = dict(
        date=datetime(2020, 3, 22, 19, 49, 57, 1),
        url="https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/",
        tags=["indieweb", "static", "webmentions"],
        title='Some title',
        comment="Adding Webmention Support to a Static Site"
    )

    bookmark = Bookmark(bookmark_dict)

    expected = """+++
date = "2020-03-22T19:49:57+01:00"
signet = "https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/"
title = "Some title"
bookmarktags = ["indieweb", "static", "webmentions"]
+++

Adding Webmention Support to a Static Site
"""
    assert expected == bookmark.format(formater)

def test_title_has_double_quotes():
    bookmark_dict = dict(
        date=datetime(2020, 3, 22, 19, 49, 57, 1),
        url="https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/",
        tags=["indieweb", "static", "webmentions"],
        title='Some "perfid" title',
        comment="Adding Webmention Support to a Static Site"
    )

    bookmark = Bookmark(bookmark_dict)

    expected = """+++
date = "2020-03-22T19:49:57+01:00"
signet = "https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/"
title = "Some perfid title"
bookmarktags = ["indieweb", "static", "webmentions"]
+++

Adding Webmention Support to a Static Site
"""
    assert expected == bookmark.format(formater)


def test_without_title():
    bookmark_dict = dict(
        date=datetime(2020, 3, 22, 19, 49, 57, 1),
        url="https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/",
        tags=["indieweb", "static", "webmentions"],
        comment="Adding Webmention Support to a Static Site"
    )

    bookmark = Bookmark(bookmark_dict)

    expected = """+++
date = "2020-03-22T19:49:57+01:00"
signet = "https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/"
title = ""
bookmarktags = ["indieweb", "static", "webmentions"]
+++

Adding Webmention Support to a Static Site
"""
    assert expected == bookmark.format(formater)
