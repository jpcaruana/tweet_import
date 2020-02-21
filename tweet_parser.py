# -*- coding: utf-8 -*-
from datetime import datetime


def format_tweet_url(author, tweet_id):
    return f"https://twitter.com/{author}/status/{tweet_id}"


class Tweet():
    def __init__(self, tweet_as_dict: dict, author: str, user_class: str = 'twitter_user'):
        self.dict = tweet_as_dict
        self.author = author
        self.user_class = user_class

    @property
    def id(self):
        return self.dict.get('id')

    @property
    def date(self):
        return datetime.strptime(self.dict.get('created_at'), "%a %b %d %H:%M:%S +0000 %Y")

    @property
    def text(self):
        return self.dict.get('full_text')

    @property
    def lang(self):
        return self.dict.get('lang')

    @property
    def original_url(self):
        return format_tweet_url(self.author, self.id)

    @property
    def htmltext(self):
        return self.dict.get('full_text')

    @property
    def hashtags(self):
        hashtags = self.dict.get('entities', {}).get('hashtags', [])
        return set([h.get('text') for h in hashtags])

    @property
    def linked_urls(self):
        urls = self.dict.get('entities', {}).get('urls', [])
        return set([h.get('expanded_url') for h in urls])

    @property
    def retweeted(self):
        return self.dict.get('retweeted')

    @property
    def favorited(self):
        return self.dict.get('favorited')

    @property
    def retweets(self) -> int:
        return int(self.dict.get('retweet_count'))

    @property
    def favorites(self) -> int:
        return int(self.dict.get('favorite_count'))

    @property
    def is_reply(self) -> bool:
        return 'in_reply_to_status_id' in self.dict

    @property
    def replied_to_url(self) -> str:
        return format_tweet_url(self.dict.get('in_reply_to_screen_name'), self.dict.get('in_reply_to_status_id'))
