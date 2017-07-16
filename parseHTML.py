import requests

page = requests.get('https://admin.washcoll.edu/schedules/17SPschedules.html')

print(page.content)
