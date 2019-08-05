import requests
import time

url = 'https://www.reddit.com/r/ProgrammerHumor/new/.json'

def get_json(url):
    r = requests.get(url)
    while(r.status_code==429):
        # 429: Too many requests
        r = requests.get(url)
    return r

def scrap_new_elem(json1,json2):
    diff_list=[]
    for elem1 in json1['data']['children']:
        for elem2 in json2['data']['children']:
            if elem1['data']['id']!= elem2['data']['id']:
                diff_list.append(elem2)
            else:
                return diff_list
    return diff_list

def get_content_link_from_array(a):
    content_links=[]
    for i in range(len(a)):
        new_d = a[i]
        try:
            post_type = new_d['data']['post_hint']
            print(post_type)
            text = new_d['data']['title']
            print(text)
            if post_type=='image':
                content_link = new_d['data']['url']
                print(content_link)
                content_links.append({'link': content_link, 'type': 'image'})
            elif post_type=='hosted:video':
                content_link = new_d['data']['media']['reddit_video']['fallback_url']
                print(content_link)
                content_links.append({'link': content_link, 'type': 'video'})
        except KeyError:
            pass
    return content_links

def timer(url, sec):
    json1 = get_json(url)
    time.sleep(sec)
    json2 = get_json(url)
    new_elements = scrap_new_elem(json1,json2)
    if new_elements:
        content_links = get_content_link_from_array(new_elements)

