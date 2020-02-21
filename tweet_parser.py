# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Iterable


def format_tweet_url(author: str, tweet_id: str) -> str:
    """
    Re-create the full URL for a tweet

    :param author: author of the twwet
    :param tweet_id:  twitter internal ID of the tweet
    :return: real life URL of this tweet
    """
    return f"https://twitter.com/{author}/status/{tweet_id}"


class Tweet():
    def __init__(self, tweet_as_dict: dict, author: str, user_class: str = 'twitter_user'):
        """
        Create a tweet from its reprensentation (use json.loads with the exported js from Twitter

        :param tweet_as_dict: parsed json of the tweet
        :param author: author name of the tweet (the @something part)
        :param user_class: (optional) useful when you want simple HTML version of the tweet. Defaults to 'twitter_user'
        """
        self.dict = tweet_as_dict
        self.author = author
        self.user_class = user_class

    @property
    def id(self) -> str:
        return self.dict.get('id')

    @property
    def date(self) -> datetime:
        return datetime.strptime(self.dict.get('created_at'), "%a %b %d %H:%M:%S +0000 %Y")

    @property
    def text(self) -> str:
        return self.dict.get('full_text')

    @property
    def lang(self) -> str:
        return self.dict.get('lang')

    @property
    def original_url(self) -> str:
        return format_tweet_url(self.author, self.id)

    @property
    def htmltext(self) -> str:
        return self.dict.get('full_text')  # TODO

    @property
    def hashtags(self) -> Iterable[str]:
        hashtags = self.dict.get('entities', {}).get('hashtags', [])
        return set([h.get('text') for h in hashtags])

    @property
    def linked_urls(self) -> Iterable[str]:
        urls = self.dict.get('entities', {}).get('urls', [])
        return set([u.get('expanded_url') for u in urls])

    @property
    def linked_photos(self) -> Iterable[str]:
        medias = self.dict.get('entities', {}).get('media', [])
        return set([m.get('media_url_https') for m in medias if m.get('type') == 'photo'])

    @property
    def retweeted(self) -> bool:
        return self.dict.get('retweeted', False)

    @property
    def favorited(self) -> bool:
        return self.dict.get('favorited', False)

    @property
    def retweets(self) -> int:
        return int(self.dict.get('retweet_count', 0))

    @property
    def favorites(self) -> int:
        return int(self.dict.get('favorite_count', 0))

    @property
    def is_reply(self) -> bool:
        return 'in_reply_to_status_id' in self.dict

    @property
    def replied_to_url(self) -> str:
        return format_tweet_url(self.dict.get('in_reply_to_screen_name'), self.dict.get('in_reply_to_status_id'))
