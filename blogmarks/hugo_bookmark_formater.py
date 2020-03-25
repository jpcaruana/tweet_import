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
        date=bookmark.date.strftime('%Y-%m-%dT%H:%M:%S+01:00'),
        content=format_content(bookmark.comment),
        tags=format_list(bookmark.tags),
        url=bookmark.url,
        title=format_content(bookmark.title),
    )


def format_content(text: str) -> str:
    content = text.replace('\n', '\n\n')
    content = content.replace('"', '')
    content = content.replace('\\', '\\\\')
    content = content.replace('[', '')
    content = content.replace(']', '')
    return content


def format_list(elements: Iterable[str]) -> str:
    return '[' + ', '.join(['"' + e + '"' for e in sorted(elements)]) + ']'
