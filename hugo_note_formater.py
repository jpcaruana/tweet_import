# -*- coding: utf-8 -*-
from typing import Iterable

from tweet_parser import Tweet

TEMPLATE = """+++
date = "{date}"
title = "{title}"
slug = ""
categories = ["twitter"]
tags = {tags}
+++

{content}
"""


def formater(tweet: Tweet) -> str:
    return TEMPLATE.format(
        date=tweet.date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        title=tweet.text,
        content=format_content(tweet),
        tags=format_list(tweet.hashtags),
    )


def format_content(tweet):
    content = tweet.text
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
