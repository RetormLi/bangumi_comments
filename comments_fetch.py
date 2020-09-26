#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import random
import re
import json
from datetime import datetime

# Put your userid here
user_id = 'retormli'

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]
page_re = re.compile(r"<a href=\"/anime/list/.*?/collect\?page=([0-9]+)\" class=\"p\">[0-9]+</a>", re.UNICODE)
item_re = re.compile(
    r"<a href=\"/subject/[0-9]+\" class=\"l\">(.*?)</a>.*?<span class=\"starlight stars([0-9]+)\">.*?style=\".*?\"><div class=\"text\"> (.*?)<",
    re.UNICODE)
url = r"https://bangumi.tv/anime/list/" + user_id + "/collect"
date_time = str(datetime.now().date())
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
save_path = 'comments_' + user_id + '_' + date_time + '.json'


def get_item(pair, d):
    name, star, comment = pair
    if name not in d:
        d[name] = {'star': star, 'comment': comment, 'time': time}
        return
    if d[name]['star'] != star:
        if 'history_star' in d[name]:
            d[name]['history_star'].update({d[name]['time']: d[name]['star']})
        else:
            d[name]['history_star'] = {d[name]['time']: d[name]['star']}
        d[name]['star'] = star
        d[name]['time'] = time
    if d[name]['comment'] != comment:
        if 'history_comment' in d[name]:
            d[name]['history_comment'].update({d[name]['time']: d[name]['comment']})
        else:
            d[name]['history_comment'] = {d[name]['time']: d[name]['comment']}
        d[name]['comment'] = comment
        d[name]['time'] = time
    return


if __name__ == '__main__':
    headers = dict()
    try:
        with open(save_path, 'r', encoding='utf-8') as json_file:
            storage = json.load(json_file)
    except FileNotFoundError:
        storage = dict()
    headers['User-Agent'] = random.choice(user_agent_list)

    print('Begin Fetching...')
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    text = r.text.replace('\n', '').replace('\r', '')
    page_num = int(page_re.findall(text)[-1])
    print('Page 1 get.')

    re_list = item_re.findall(text)
    for re_tuple in re_list:
        # print(re_tuple[0] + ' fetched.')
        get_item(re_tuple, storage)

    if page_num > 1:
        for i in range(2, page_num + 1):
            url = url + "?page=" + str(i)
            headers['User-Agent'] = random.choice(user_agent_list)

            r = requests.get(url, headers=headers)
            r.encoding = 'utf-8'
            text = r.text.replace('\n', '').replace('\r', '')
            print('Page ' + str(i) + ' get.')

            re_list = item_re.findall(text)
            for re_tuple in re_list:
                # print(re_tuple[0] + ' fetched.')
                get_item(re_tuple, storage)

    with open(save_path, 'w', encoding='utf-8') as json_file:
        print('Saving...')
        json.dump(storage, json_file, ensure_ascii=False, indent=4)
        print('Everything is OK.')
