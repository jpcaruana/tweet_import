#! /usr/bin/env python
import json
from pathlib import Path

import click

from blogmarks.blogmarks_parser import Bookmark, parser
from blogmarks.hugo_bookmark_formater import formater as bookmark_formater
from tweet.hugo_note_formater import formater as note_formater
from tweet.tweet_parser import Tweet


def write_note_file(tweet_dict):
    tweet = Tweet(tweet_dict, author='jpcaruana')
    dir_path = f"content/notes/{tweet.date.strftime('%Y/%m/%d')}"
    file_path = f"{dir_path}/{tweet.date.strftime('%H-%M.md')}"
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as dest:
        dest.writelines(tweet.format(note_formater))


def write_bookmark_file(bookmark):
    dir_path = f"content/bookmarks/{bookmark.date.strftime('%Y/%m/%d')}"
    file_path = f"{dir_path}/{bookmark.entry_id}.md"
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as dest:
        dest.writelines(bookmark.format(bookmark_formater))


@click.group()
def main():
    pass


@main.command('import-tweets-into-hugo-notes')
@click.argument('source_file')
def import_tweets_into_hugo_notes(source_file):
    with open(source_file, 'r') as source:
        posts = json.loads(source.read())
        for post in posts:
            write_note_file(post.get('tweet'))


@main.command('import-blogmarks-into-hugo-bookmarks')
@click.argument('source_file')
def import_tweets_into_hugo_notes(source_file):
    with open(source_file, 'r') as source:
        bookmarks = parser(source.read())
        for bookmark in bookmarks:
            write_bookmark_file(bookmark)


if __name__ == '__main__':
    main()
