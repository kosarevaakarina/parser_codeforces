import requests
from codeforces.models import TaskCodeforces


def parser_codeforces(url: str) -> None:
    """Осуществляет парсинг сайта Codeforces и создает экземпляры модели TaskCodeforces"""
    response = requests.get(url=url)
    data = response.json()
    for i in range(len(data['result']['problems'])):
        title = data['result']['problems'][i]['name']
        contest_id = data['result']['problems'][i]['contestId']
        index = data['result']['problems'][i]['index']
        tags_list = data['result']['problems'][i]['tags']
        tags = ', '.join(tags_list)
        rating = data['result']['problems'][i].get('rating')
        solved_count = data['result']['problemStatistics'][i]['solvedCount']
        result = {
            "title": title,
            "task_url": f'https://codeforces.com/problemset/problem/{contest_id}/{index}',
            "contest_id": contest_id,
            "index": index,
            "tags": tags,
            "rating": rating,
            "solved_count": solved_count
        }
        TaskCodeforces.objects.update_or_create(**result)
