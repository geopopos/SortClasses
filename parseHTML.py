import requests

def getSubstring(string, index1, index2):
    substring = ""
    for i in range(index1, index2):
        substring += string[i]
    return substring

page = requests.get('https://admin.washcoll.edu/schedules/17SPschedules.html')

html = page.content

courseIndex = html.find('k">AMS', 0, len(html))
courseEnd = html.find("\n", courseIndex, len(html))
courseString = getSubstring(html, courseIndex+3, courseEnd)
    

courseNumIndex = courseString.find(" ", 0, len(courseString))
courseNumber = getSubstring(courseString, courseNumIndex+1, courseNumIndex+4)
courseSection = getSubstring(courseString, courseNumIndex+5, courseNumIndex+7)
print(courseSection)
