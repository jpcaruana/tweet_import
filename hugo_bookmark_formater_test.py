# -*- coding: utf-8 -*-
from blogmarks_parser import Bookmark
from hugo_bookmark_formater import formater


def test_x():
    bookmark_dict = dict(
        date="2020-03-22T19:49:57+01:00",
        url="https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/",
        tags=["indieweb", "static", "webmentions"],
        comment="Adding Webmention Support to a Static Site"
    )

    bookmark = Bookmark(bookmark_dict)

    expected = """+++
date = "2020-03-22T19:49:57+01:00"
signet = "https://keithjgrant.com/posts/2019/02/adding-webmention-support-to-a-static-site/"
bookmarktags = ["indieweb", "static", "webmentions"]
+++

Adding Webmention Support to a Static Site
"""
    assert expected == bookmark.format(formater)
