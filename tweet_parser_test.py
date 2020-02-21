# -*- coding: utf-8 -*-
from datetime import datetime

from tweet_parser import Tweet


def test_read_tweet_rt():
    tweet_dict = {
        'retweeted': False,
        'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
        'entities': {
            'hashtags': [
                {'text': 'leanagileCamp', 'indices': ['74', '88']},
                {'text': 'some_hashtag', 'indices': ['74', '88']}
            ],
            'symbols': [],
            'user_mentions': [
                {'name': 'Bruno Thomas', 'screen_name': 'bam_thomas', 'indices': ['18', '29'],
                 'id_str': '213077589', 'id': '213077589'}
            ],
            'urls': [
                {'url': 'http://t.co/lv60oyicwD', 'expanded_url': 'http://leanagilecamp.fr',
                 'display_url': 'leanagilecamp.fr', 'indices': ['51', '73']},
                {'url': 'http://t.co/toto', 'expanded_url': 'https://sommeurl.fr',
                 'display_url': 'someurl.fr', 'indices': ['51', '73']}
            ]
        },
        'display_text_range': ['0', '89'],
        'favorite_count': '1',
        'in_reply_to_status_id_str': '354943502657929216',
        'id_str': '354957091389181952',
        'in_reply_to_user_id': '213077589',
        'truncated': False,
        'retweet_count': '0',
        'id': '354957091389181952',
        'in_reply_to_status_id': '354943502657929216',
        'possibly_sensitive': False,
        'created_at': 'Wed Jul 10 13:35:40 +0000 2013',
        'favorited': True,
        'full_text': 'Beau boulot ! RT “@bam_thomas: En ligne tout chaud http://t.co/lv60oyicwD #leanagileCamp”',
        'lang': 'fr',
        'in_reply_to_screen_name': 'bam_thomas',
        'in_reply_to_user_id_str': '213077589'
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    assert tweet.id == '354957091389181952'
    assert tweet.text == 'Beau boulot ! RT “@bam_thomas: En ligne tout chaud http://t.co/lv60oyicwD #leanagileCamp”'
    assert tweet.lang == 'fr'
    assert tweet.date == datetime(2013, 7, 10, 13, 35, 40)
    assert tweet.hashtags == set(['leanagileCamp', 'some_hashtag'])
    assert tweet.linked_urls == set(['http://leanagilecamp.fr', 'https://sommeurl.fr'])
    assert tweet.linked_photos == set()
    assert not tweet.retweeted
    assert tweet.retweets == 0
    assert tweet.favorited
    assert tweet.favorites == 1
    assert tweet.original_url == 'https://twitter.com/jpcaruana/status/354957091389181952'
    assert tweet.is_reply
    assert tweet.replied_to_url == 'https://twitter.com/bam_thomas/status/354943502657929216'

    # hors sujet : a mettre dans le formatter
    # assert tweet.htmltext == 'Beau boulot ! RT “<a href="https://twitter.com/bam_thomas" class="twitter_user">@bam_thomas</a>:' \
    #                         ' En ligne tout chaud <a href="http://leanagilecamp.fr">leanagilecamp.fr</a> #leanagileCamp”'


def test_retweet_with_images():
    tweet_dict = {
        "retweeted": False,
        "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
        "entities": {
            "user_mentions": [{
                "name": "Jean-Moundir",
                "screen_name": "supermegadrivin",
                "indices": ["3", "19"],
                "id_str": "108570813",
                "id": "108570813"
            }],
            "urls": [],
            "symbols": [],
            "media": [{
                "expanded_url": "https://twitter.com/supermegadrivin/status/281717403589693440/photo/1",
                "source_status_id": "281717403589693440",
                "indices": ["37", "57"],
                "url": "http://t.co/RQFLc0hW",
                "media_url": "http://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg",
                "id_str": "281717403593887744",
                "source_user_id": "108570813",
                "id": "281717403593887744",
                "media_url_https": "https://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg",
                "source_user_id_str": "108570813",
                "sizes": {
                    "medium": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    },
                    "thumb": {
                        "w": "150",
                        "h": "150",
                        "resize": "crop"
                    },
                    "large": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    },
                    "small": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    }
                },
                "type": "photo",
                "source_status_id_str": "281717403589693440",
                "display_url": "pic.twitter.com/RQFLc0hW"
            }],
            "hashtags": []
        },
        "display_text_range": ["0", "57"],
        "favorite_count": "0",
        "id_str": "281738246252285954",
        "truncated": False,
        "retweet_count": "0",
        "id": "281738246252285954",
        "possibly_sensitive": False,
        "created_at": "Thu Dec 20 12:30:07 +0000 2012",
        "favorited": False,
        "full_text": "RT @supermegadrivin: La fin du monde http://t.co/RQFLc0hW",
        "lang": "fr",
        "extended_entities": {
            "media": [{
                "expanded_url": "https://twitter.com/supermegadrivin/status/281717403589693440/photo/1",
                "source_status_id": "281717403589693440",
                "indices": ["37", "57"],
                "url": "http://t.co/RQFLc0hW",
                "media_url": "http://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg",
                "id_str": "281717403593887744",
                "source_user_id": "108570813",
                "id": "281717403593887744",
                "media_url_https": "https://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg",
                "source_user_id_str": "108570813",
                "sizes": {
                    "medium": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    },
                    "thumb": {
                        "w": "150",
                        "h": "150",
                        "resize": "crop"
                    },
                    "large": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    },
                    "small": {
                        "w": "375",
                        "h": "243",
                        "resize": "fit"
                    }
                },
                "type": "photo",
                "source_status_id_str": "281717403589693440",
                "display_url": "pic.twitter.com/RQFLc0hW"
            }]
        }
    }

    tweet = Tweet(tweet_dict, author='jpcaruana')

    assert tweet.id == '281738246252285954'
    assert tweet.text == "RT @supermegadrivin: La fin du monde http://t.co/RQFLc0hW"
    assert tweet.hashtags == set()
    assert tweet.linked_urls == set()
    assert tweet.linked_photos == set(['https://pbs.twimg.com/media/A-jcfGhCUAA6GDW.jpg'])
