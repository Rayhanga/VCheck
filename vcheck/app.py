from vcheck import VCheck
import json

def run():
    module = VCheck()

    while(not module.auth):
        module.login(input('Username: '), input('Password: '))

        if module.auth:
            print('Login Successful')
        else:
            print('Login Failed')

    print('Upcoming Tasks')
    for task in module.getUpcomingTasks():
        print(json.dumps(task, indent=2))

    print('Course Status')
    for course in module.getCourseList():
        print(json.dumps(course, indent=2))

    module.endConnection()