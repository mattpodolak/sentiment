import requests
def news_search(keyword, date_str):
    url = ('https://newsapi.org/v2/everything?'
        'q='+keyword+'&'
        'from=2018-08-20&'
        'to=2018-08-20&'
        'language=en&'
        'sortBy=popularity&'
        'apiKey=a81c4da648bd4945ba2a4d15413ff608')
    response = requests.get(url)
    r = response.json()
    title_array = []
    for titles in r['articles']:
        title_array.append(titles['title'])
    title_array = title_array[0:31]
    return title_array
