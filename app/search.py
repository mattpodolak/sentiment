import requests
def news_search(keyword, date_str):
    url = ('https://newsapi.org/v2/everything?'
        'q='+keyword+'&'
        'from='+date_str+'&'
        'to='+date_str+'&'
        'language=en&'
        'sortBy=popularity&'
        'apiKey=b33925218d90423a9e742920006e9c75')
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
