import datetime
from bs4 import BeautifulSoup as bs

def filterCourseName(course_name):
    # Filter course name
    ## Soft filter
    softFilter = course_name.replace('Course name', '').replace('Course is starred', '').replace(' ','').replace('\n', '')
    ## Hard filter
    string = list(softFilter)
    temp = []
    c = 0
    for i in range(len(string)):
        if string[i] == '|':
            c += 1
        if c < 3 and c > 1:
            temp.append(string[i])
    ### Append some blank spaces
    string = ''.join(temp).replace('|', '').replace('(*)','').replace('#', '').replace('/','')
    temp = []
    for i in range(len(string)):
        if (string[i].isupper() or string[i].isdigit()) and i != 0:
            temp.append(' ')
        try:
            if string[i]+string[i+1]+string[i+2] == 'dan':
                temp.append(' ')
        except:
            pass
        temp.append(string[i])
    hardFilter = ''.join(temp)
    tahun_ajar = softFilter[3:12]

    if softFilter[:3] == 'ATA':
        tahun = tahun_ajar[-4:]
    else:
        tahun = tahun_ajar[:4]
        
    return [hardFilter, tahun]

def getCourseList(page_source):
    # Get general info from enrolled course
    sauce = bs(page_source, 'html.parser')
    cList = sauce.findAll('li', {'class': 'course-listitem'})
    data = []

    for course in cList:
        # Get anchor tag from html
        cItem = course.find('a', {'class': 'coursename'})

        # Course progress percentage
        try:
            progress = course.find('strong').text
        except:
            progress = None

        # Course name
        name = filterCourseName(cItem.text)[0]

        # Course link
        id = cItem.attrs.get('href')[-4:]

        # Pack valuable info into a dictionary
        data.append({
            'courseId': id,
            'courseName': name,
            'courseProgress': progress
        })

    return(data)

def getCourseData(page_source):
    # Collect material, assignments (finished / unfinished) from specific course
    sauce = bs(page_source, 'html.parser')
    topicList = sauce.find('ul', {'class': 'topics'}).findChildren('li', {'class': 'section main clearfix'})

    completed = 'https://v-class.gunadarma.ac.id/theme/image.php/boost/core/1585289926/i/completion-manual-y'

    for topic in topicList:
        topicName = topic.attrs.get('aria-label')
        print(topic, '\n')
          
def getUpcomingTask(page_source):
    # Get upcoming task
    sauce = bs(page_source, 'html.parser')
    taskList = sauce.find('div', {'class': 'eventlist my-1'}).findChildren('div', {'class': 'event m-t-1'})
    data = []

    for task in taskList:
        now = datetime.datetime.now()
        taskInfo = task.findAll('a')
        today = now.strftime('%A, %d %B')
        tomorrow = (now + datetime.timedelta(days=1)).strftime('%A, %d %B')
        year = filterCourseName(taskInfo[-2].text)[1]
        title = task.find('h3', {'class': 'name d-inline-block'}).text

        taskMatkul = filterCourseName(taskInfo[-2].text)[0]

        taskDeadline = taskInfo[0].parent.text.replace('Today', today).replace('Tomorrow', tomorrow) + ', ' + year
        taskDeadline = datetime.datetime.strptime(taskDeadline, '%A, %d %B, %I:%M %p, %Y')

        taskUrl = taskInfo[-1].attrs.get('href')

        taskDesc = task.find('div', {'class': 'description-content'})
        if taskDesc:
            taskDesc = taskDesc.find('div')

        if 'quiz' in taskUrl:
            taskType = 'Quiz'
        elif 'forum' in taskUrl:
            taskType = 'Forum'
        elif 'assign' in taskUrl:
            taskType = 'Assignment'
        else:
            taskType = None

        if 'closes' in title or 'due' in title or 'should be completed' in title:
            data.append({
                'taskMatkul': taskMatkul,
                'taskDeadline': taskDeadline.strftime('%d-%m-%Y %H:%M:%S'),
                'taskUrl': taskUrl,
                'taskType': taskType
            })

    return data

def getLoginInfo(page_source):
    sauce = bs(page_source, 'html.parser')
    error = sauce.find('div', {'class': 'loginerrors'})

    if error:
        return False
    else:
        return True