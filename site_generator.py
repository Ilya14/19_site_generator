import os
import json
import datetime
import logging
import markdown2

from jinja2 import Environment, FileSystemLoader


def load_config(config_file):
    with open(config_file, 'r') as file_handler:
        return json.load(file_handler)


def get_articles_data(config):
    articles_data = {}
    for topic in config['topics']:
        topic_articles = []
        for article in config['articles']:
            if topic['slug'] == article['topic']:
                topic_article_data = {
                    'article_title': article['title'],
                    'article_md_source': os.path.join('articles', article['source']),
                    'article_html_source': os.path.join('articles', article['source'].replace('.md', '.html'))
                }
                topic_articles.append(topic_article_data)
        articles_data[topic['title']] = topic_articles
    return articles_data


def get_markdown_article(article_md_file_name):
    return markdown2.markdown_path(article_md_file_name)


def generate_index_page(articles_data):
    templates_dir = 'templates'
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('index')

    template_params = {
        'page_title': 'Энциклопедия',
        'project_name': 'DEVMAN',
        'title': 'Энциклопедия',
        'text': 'Сборник полезных материалов по языку программирования Python',
        'topics': articles_data,
        'year': datetime.datetime.now().year,
        'company': 'Devman, Inc.'
    }

    index_dir = os.path.join('site', 'index.html')
    with open(index_dir, 'w') as file_handler:
        file_handler.write(template.render(template_params))

    logging.info('Index page has been created')


def generate_article_page(topic_title, article_title, article_html_file_name, article_text):
    templates_dir = 'templates'
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('article')

    template_params = {
        'page_title': article_title,
        'project_name': 'DEVMAN',
        'topic_title': topic_title,
        'article_title': article_title,
        'article_text': article_text,
        'year': datetime.datetime.now().year,
        'company': 'Devman, Inc.'
    }

    article_dir = os.path.dirname(article_html_file_name)
    if not os.path.exists(article_dir):
        os.makedirs(article_dir)

    with open(article_html_file_name, 'w') as file_handler:
        file_handler.write(template.render(template_params))

    logging.info('Article "%s/%s" has been created', topic_title, article_title)


def generate_articles_pages(articles_data):
    for topic in articles_data:
        for article in articles_data[topic]:
            article_html = get_markdown_article(article['article_md_source'])
            generate_article_page(
                topic,
                article['article_title'],
                os.path.join('site', article['article_html_source']),
                article_html
            )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=u'[%(filename)s#] %(levelname)-8s [%(asctime)s] %(message)s',
        datefmt=u'%m/%d/%Y %I:%M:%S %p'
    )

    config_file_name = 'config.json'
    config = load_config(config_file_name)
    articles_data = get_articles_data(config)
    generate_index_page(articles_data)
    generate_articles_pages(articles_data)
