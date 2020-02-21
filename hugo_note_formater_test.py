# -*- coding: utf-8 -*-
from hugo_note_formater import formater
from tweet_parser import Tweet


def test_format_simple_note():
    tweet_dict = {
        'id': '354957091389181952',
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'full_text': 'Ceci est un petit tweet',
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    expected = """+++
date = "2013-07-10T13:35:40Z"
title = "Ceci est un petit tweet"
slug = ""
categories = ["twitter"]
tags = []
+++

Ceci est un petit tweet
"""
    assert expected == tweet.format(formater)


def test_format_note_with_tags():
    tweet_dict = {
        'entities': {
            'hashtags': [
                {'text': 'leanagileCamp', 'indices': ['74', '88']},
                {'text': 'some_hashtag', 'indices': ['74', '88']}],
        },
        'id': '354957091389181952',
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'full_text': 'Ceci est un petit tweet',
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    expected = """+++
date = "2013-07-10T13:35:40Z"
title = "Ceci est un petit tweet"
slug = ""
categories = ["twitter"]
tags = ["leanagileCamp", "some_hashtag"]
+++

Ceci est un petit tweet
"""
    assert expected == tweet.format(formater)


def test_format_note_with_an_url():
    tweet_dict = {
        'entities': {
            'urls': [
                {'url': 'http://t.co/lv60oyicwD', 'expanded_url': 'http://leanagilecamp.fr',
                 'display_url': 'leanagilecamp.fr', 'indices': ['51', '73']}
            ]
        },
        'id': '354957091389181952',
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'full_text': 'Ceci est un petit tweet http://t.co/lv60oyicwD',
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    expected = """+++
date = "2013-07-10T13:35:40Z"
title = "Ceci est un petit tweet http://t.co/lv60oyicwD"
slug = ""
categories = ["twitter"]
tags = []
+++

Ceci est un petit tweet [leanagilecamp.fr](http://leanagilecamp.fr)
"""
    assert expected == tweet.format(formater)


def test_format_note_with_user_mentions():
    tweet_dict = {
        'entities': {
            'user_mentions': [
                {'name': 'Bruno Thomas', 'screen_name': 'bam_thomas', 'indices': ['18', '29'],
                 'id_str': '213077589', 'id': '213077589'}
            ],
        },
        'id': '354957091389181952',
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'full_text': 'Ceci est un petit tweet avec @bam_thomas',
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    expected = """+++
date = "2013-07-10T13:35:40Z"
title = "Ceci est un petit tweet avec @bam_thomas"
slug = ""
categories = ["twitter"]
tags = []
+++

Ceci est un petit tweet avec [@bam_thomas](https://twitter.com/bam_thomas)
"""
    assert expected == tweet.format(formater)


def test_format_note_with_images():
    tweet_dict = {
        'entities': {
            "media": [
                {
                    "media_url_https": "https://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg",
                    "type": "photo",
                },
                {
                    "media_url_https": "https://pbs.twimg.com/media/another.jpg",
                    "type": "photo",
                }],
        },
        'id': '354957091389181952',
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'full_text': 'Ceci est un petit tweet avec images',
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    expected = """+++
date = "2013-07-10T13:35:40Z"
title = "Ceci est un petit tweet avec images"
slug = ""
categories = ["twitter"]
tags = []
+++

Ceci est un petit tweet avec images

{{< figure src="https://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg" >}}

{{< figure src="https://pbs.twimg.com/media/another.jpg" >}}
"""
    assert expected == tweet.format(formater)
