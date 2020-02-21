#! /usr/bin/env python
import json
from pathlib import Path

import click

import hugo_note_formater
from tweet_parser import Tweet


def write_note_file(tweet_dict):
    tweet = Tweet(tweet_dict, author='jpcaruana')
    dir_path = f"content/notes/{tweet.date.strftime('%Y/%m/%d')}"
    file_path = f"{dir_path}/{tweet.date.strftime('%H-%M.md')}"
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as dest:
        dest.writelines(tweet.format(hugo_note_formater.formater))


@click.group()
def main():
    pass


@main.command('import-into-hugo-notes')
@click.argument('source_file')
def import_into_hugo_notes(source_file):
    with open(source_file, 'r') as source:
        posts = json.loads(source.read())
        for post in posts:
            write_note_file(post.get('tweet'))
            return


if __name__ == '__main__':
    main()
