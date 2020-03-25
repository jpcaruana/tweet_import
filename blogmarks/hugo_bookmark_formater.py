# -*- coding: utf-8 -*-
from typing import Iterable

from blogmarks.blogmarks_parser import Bookmark

TEMPLATE = """+++
date = "{date}"
signet = "{url}"
title = "{title}"
bookmarktags = {tags}
+++

{content}
"""


def formater(bookmark: Bookmark) -> str:
    return TEMPLATE.format(
        date=bookmark.date,
        content=format_content(bookmark),
        tags=format_list(bookmark.tags),
        url=bookmark.url,
        title=bookmark.title
    )


def format_content(bookmark: Bookmark) -> str:
    content = bookmark.comment.replace('\n', '\n\n')
    content = content.replace(r'[', '\\[')
    content = content.replace(']', '\\]')
    return content


def format_list(elements: Iterable[str]) -> str:
    return '[' + ', '.join(['"' + e + '"' for e in sorted(elements)]) + ']'
