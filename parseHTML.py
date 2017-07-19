import requests
import bubbleSort

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
courseDepartment = []
courseNumber = []
courseSection = []
courseDays = []
courseTimes = []
courseTimesValue = []
courseIndex = 0
a = 0;

#Find all courses in a certain department and store their data to their specified arrays
while(courseIndex != -1):
    courseIndex = html.find('k">' + department, lastIndex, len(html))
    courseDepartment.append(department);
    if(courseIndex != -1):
        courseEnd = html.find("\n", courseIndex, len(html))
        lastIndex = courseEnd;
        courseString = getSubstring(html, courseIndex+3, courseEnd)
        courseNumIndex = courseString.find(" ", 0, len(courseString))
        

        courseNumber.append(getSubstring(courseString, courseNumIndex+1, courseNumIndex+4))
        courseSection.append(getSubstring(courseString, courseNumIndex+5, courseNumIndex+7))
        courseDays.append(getSubstring(courseString, 58, courseString.find(" ", 58, len(courseString))))
        courseTimes.append(getSubstring(courseString, 65, courseString.find(" ", 65, len(courseString))))
        if(courseTimes[a][5] == "A"):
            courseTimesValue.append(int(courseTimes[a][0] + courseTimes[a][1]))
        elif(courseTimes[a][5] == "P"):
            courseTimesValue.append(12+int(courseTimes[a][0] + courseTimes[a][1])%12)
        a+=1;

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []

#Organize Classes By Day
for i in range(0, len(courseDays)):
    for j in range(0, len(courseDays[i])):
        if(courseDays[i][j] == "M"):
            monday.append(i)
        elif(courseDays[i][j] == "W"):
            wednesday.append(i)
        elif(courseDays[i][j] == "F"):
            friday.append(i)
        elif(courseDays[i][j] == "T"):
            if(j+1 > len(courseDays[i])):
                tuesday.append(i)
            elif(courseDays[i][j+1] == "T"):
                tuesday.append(i)
            elif(courseDays[i][j+1] == "H"):
                thursday.append(i);

dayLabel = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day = [monday, tuesday, wednesday, thursday, friday]

#Sort Classes By Time
bubbleSort.bubbleSort(day, courseTimesValue);


#Print Classes
for i in range(0, len(day)):
    print (dayLabel[i])
    print("_________________________")
    for j in range(0, len(day[i])):
        index = day[i][j]
        print(courseDepartment[index] + " " + str(courseNumber[index]) + " " + str(courseSection[index]) + " " + courseDays[index] + "     " + courseTimes[index])
    print("\n")
