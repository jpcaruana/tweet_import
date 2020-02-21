# -*- coding: utf-8 -*-
from typing import Iterable

from tweet_parser import Tweet

TEMPLATE = """+++
date = "{date}"
title = "{title}"
categories = ["twitter"]
tags = {tags}
original_url = "{original_url}"
+++

{content}
"""


def formater(tweet: Tweet) -> str:
    return TEMPLATE.format(
        date=tweet.date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        title=format_title(tweet),
        content=format_content(tweet),
        tags=format_list(tweet.hashtags),
        original_url=tweet.original_url,
    )


def format_title(tweet):
    title = tweet.text.split('\n')[0]
    title = title.replace('[', '')
    title = title.replace(']', '')
    return title


def format_content(tweet):
    content = tweet.text.replace('\n', '\n\n')
    content = content.replace(r'[', '\\[')
    content = content.replace(']', '\\]')
    for url in tweet.complete_urls:
        content = content.replace(url.get('url'), f"[{url.get('display_url')}]({url.get('expanded_url')})")
    for um in tweet.user_mentions:
        content = content.replace(f'@{um}', f"[@{um}](https://twitter.com/{um})")
    if len(tweet.linked_photos) > 0:
        content += '\n\n'
    content += '\n\n'.join(['{{< figure src="' + url + '" >}}' for url in sorted(tweet.linked_photos)])
    return content


def format_list(elements: Iterable[str]) -> str:
    return '[' + ', '.join(['"' + e + '"' for e in sorted(elements)]) + ']'
