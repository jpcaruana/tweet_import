# -*- coding: utf-8 -*-
from datetime import datetime
from io import StringIO
from typing import Iterable

import atoma


class Bookmark:
    def __init__(self, as_dict: dict):
        """
        Create a Bookmark from its representation

        :param as_dict: parsed bookmark
        """
        self.dict = as_dict

    def format(self, formatter):
        return formatter(self)

    @property
    def date(self) -> datetime:
        return self.dict.get('date')

    @property
    def entry_id(self) -> datetime:
        return self.dict.get('entry_id')

    @property
    def comment(self) -> str:
        return self.dict.get('comment').replace('\r', '\n')

    @property
    def url(self) -> str:
        return self.dict.get('url')

    @property
    def title(self) -> str:
        return self.dict.get('title')

    @property
    def tags(self) -> Iterable[str]:
        return self.dict.get('tags', [])


def parser(content_as_string):
    feed = atoma.parse_atom_file(StringIO(content_as_string))
    return (parse(e) for e in feed.entries)


def parse(entry):
    comment = ''
    if entry.content:
        comment = entry.content.value
    d = dict(
        date=entry.published,
        entry_id=entry.id_.split(':')[-1],
        url=next(u.href for u in entry.links if u.rel is None),
        title=entry.title.value,
        tags=[c.label for c in entry.categories if c.scheme == 'http://blogmarks.net/tag/'],
        comment=comment
    )
    return Bookmark(d)
