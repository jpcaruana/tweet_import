# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Iterable


class Bookmark():
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
    def content(self) -> str:
        return self.dict.get('comment').replace('\r', '\n')

    @property
    def url(self) -> str:
        return self.dict.get('url')

    @property
    def tags(self) -> Iterable[str]:
        return self.dict.get('tags', [])
