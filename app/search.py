import requests
def news_search(keyword, date_str):
    url = ('https://newsapi.org/v2/everything?'
        'q='+keyword+'&'
        'from='+date_str+'&'
        'to='+date_str+'&'
        'language=en&'
        'sortBy=popularity&'
        'apiKey=2fe31a4662ee456b9c2180ee36ef62ee')
    response = requests.get(url)
    r = response.json()
    title_array = []
    desc_array = []
    for titles in r['articles']:
        title_array.append(titles['title'])
        desc_array.append(titles['description'])
    title_array = title_array[0:31]
    desc_array = desc_array[0:31]
    return title_array, desc_array
