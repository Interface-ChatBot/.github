from flask import Flask

print('[Hello Flask!]')
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi Flask!'


@app.route('/member')  # 인터페이스 집부 안내
def member():
    return {'member1': 'Park Sang Wook',
            'member2': 'Lee Gu Ri',
            'member3': 'Dong Gi Chang',
            'member4': 'Gwang HA Yoon',
            }


@app.route('/event')  # 인터페이스 행사 안내
def event():
    return {
        'event1': 'MT',
        'event2': 'programing exhibition',
        'event3': 'Opening Meeting',
        'event4': 'Closing Meeting',
        'event5': 'Freshman MT'
    }


@app.route('/new_project/<Number_of_people>/<int:project_name>')  # 인터페이스 프로젝트 모집
def new_project(Number_of_people, project_name):
    return '{Number_of_people}({project_name})  '


@app.route('/join_project')  # 인터페이스 프로젝트 구인
def join_project():
    return {
        'list1': 'aaa',
        'list2': 'bbb',
        'list3': 'ccc',
        'list4': 'ddd'
    }


if __name__ == '__main__':
    app.run(debug=True)
