import requests

year = "17"
semester = "SP"
department = "CSI"

def getSubstring(string, index1, index2):
    substring = ""
    for i in range(index1, index2):
        substring += string[i]
    return substring

page = requests.get('https://admin.washcoll.edu/schedules/' + year + semester + 'schedules.html')

html = page.content

""" create an array for each data point:
-Course Number
-Course Section
-Course Days
-Course Time

Loop through entire string running find setting the index of that find and loop through again
"""
lastIndex = 0
courseNumber = []
courseSection = []
courseIndex = 0;

while(courseIndex != -1):
    courseIndex = html.find('k">' + department, lastIndex, len(html))
    if(courseIndex != -1):
        courseEnd = html.find("\n", courseIndex, len(html))
        lastIndex = courseEnd;
        courseString = getSubstring(html, courseIndex+3, courseEnd)
    

        courseNumIndex = courseString.find(" ", 0, len(courseString))
        courseNumber = getSubstring(courseString, courseNumIndex+1, courseNumIndex+4)
        courseSection = getSubstring(courseString, courseNumIndex+5, courseNumIndex+7)
        courseDays = getSubstring(courseString, 58, courseString.find(" ", 58, len(courseString)))
        courseTimes = getSubstring(courseString, 65, courseString.find(" ", 65, len(courseString)))
        print(courseDays)
