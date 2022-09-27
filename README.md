***
# __Interface-ChatBot__
***
## __2022 프로그래밍전시회 인터페이스 챗봇__

> 인터페이스 동아리를 안내하는 카카오톡 챗봇

## Member
* __주시환__
    - 팀장
    - 기능 구현
* __박상욱__
    - 멘토
    - 기능 구현
* __박서진__
    - 기능 구현
* __박세현__
    - 서버연동
* __이형민__
    - 서버연동
* __김건민__
    - 서기
    - DB
* __한건희__
    - 머신러닝
## 구현할 기능
1. __인터페이스 활동 일정 안내__
    - 기능구현 : 박서진
2. __인터페이스 인원 수 안내 (기수별, 현재 활동 중)__
    - 기능구현 : 박서진
3. __인터페이스 집부 구성원 안내 (번호는 검토 필요, 메일은 가능)__
    - 기능구현 : 주시환
4. __인터페이스 회비 안내__ (구현완료)
    - 기능구현 : 박상욱
5. __인터페이스 동아리 방 위치 안내__ (구현완료)
    - 기능구현 : 박상욱
6. __인터페이스 링크 안내 (깃허브, 인스타그램, 홈페이지, 앱)__
    - 기능구현 : 주시환
7. __인터페이스 소개글 (역사 등등)__
    - 기능구현 : 박서진
8. __인터페이스 행사 상세하게 소개 (사진 첨부)__
    - 기능구현 : 주시환
9. __인터페이스 동아리방 실시간 재실 인원 체크__
    - 기능구현 : 박상욱
10. __인터페이스 챗봇 도움말 (챗봇 소개글, 챗봇 기능 소개)__
    - 기능구현 : 주시환 
11. __인터페이스 동아리 방 비밀번호 안내 (학번 및 이름 체크, 악용 가능성으로 검토 필요)__
    - 기능구현 : 박상욱
12. __인터페이스 동아리에 건의사항 받는 서비스 (비품, 음식 등 필요한 물품)__
    - 기능구현 : 박서진
13. __인터페이스 동아리 방 와이파이 비밀번호 안내__ (구현완료)
    - 기능구현 : 박상욱
    
## Using
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)

## 프로젝트 설치 방법

명령프롬프트에서 아래의 코드 실행
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install flask
pip install flask-cors
python app.py
```
* [python 명령어가 작동하지 않는 경우 환경 변수 설정](https://wxmin.tistory.com/121)

## 참고자료
* [구름 IDE 이용하여 카카오톡 스킬 서버 만들기](https://novice-engineers.tistory.com/m/23)
* [카카오톡 바로가기 버튼 이용](https://luckygg.tistory.com/326)
* [카카오톡 챗봇 공식 도움말](https://i.kakao.com/docs/tutorial-chatbot-key-features#%EC%9B%B0%EC%BB%B4-%EB%B8%94%EB%A1%9Dwelcome-block-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
* [Mac 터미널 이용하여 SSH 접속 방법](https://earth-95.tistory.com/54)
***
## 회의내용
### __1차 회의__ _2022_07_30_
- __다음 회의까지(2주 뒤)__ Python Flask 서버 개발 연동해서 Hello Flask 띄우기
- __다음 회의까지(2주 뒤)__ 각자 맡은 구현할 기능을 어떻게 구현할지 생각하기
- __다음 회의까지(2주 뒤)__ 카카오톡 챗봇 채널 메뉴에 구현할 기능 구현 해보기
- 깃허브 데스크탑 ppt 정리하여 설명할 __예정__
- 8월에 각자 역할을 공부할 때는 깃허브 개인 폴더에 올릴 __예정__
- 깃허브 branch는 실제 개발 들어갈 때 사용할 __예정__
- Notion은 각자 역할 공부가 끝난 후 실제 개발이 들어가기 전에 검토할 __예정__
- 8월에는  각자 공부한 거 깃허브에 업로드 및 2주에 한 번씩 토요일 11시에 비대면(디스코드)으로 질문시간 및 회의 __예정__

### __2차 회의__ _2022_08_13_
- __다음 회의까지(2주 뒤)__ 기능 구현팀은 url을 이용하여 각자 맡은 시나리오를 완전하게 구현하는 것이 아닌 대략적으로 정보를 보여준다는 식으로 만들기
- __다음 회의까지(2주 뒤)__ DB는 Flask 와 MySQL 연동하기
- __다음 회의까지(2주 뒤)__ 서버는 Flask 와 카카오톡 챗봇이랑 연동을 하되 서버를 처음 다루고 공부하는 상태이기 때문에 무리 하지 않고 할 수 있는만큼 도전해보기
- 검토가 필요하였던 기능들은 우선 구현해보고 문제시 폐기 __예정__
- github desktop 사용법을 숙지하고 github에 각자 폴더를 만들고 2주간 공부한 파일 업로드 __완료__

### __3차 회의__ _2022_09_03_
- 회의 날짜는 금요일 6시 반으로 고정
- 회의 주기는 전 회의에서 목표로 잡은 것에 따라서 유동적으로 정할 __예정__
- 전체 회의 이외에 파트별 회의를 통해 전체 회의 날 불가피하게 불참하더라도 회의가 진행될 수 있도록 하기
- 프로젝트의 최종 목표는 서버에 올려서 배포하기
- 머신러닝은 완벽하게 구현하지 않고 유사도 검사 가능할 정도로만 구현하기
- DB 팀과 머신러닝 팀이 함께 유사도 검사 기능 구현하기
- 기능 구현 팀 : 구름 ide 로 테스트 서버 만든 후 카카오톡과 연결해서 응답 받는 것까지 목표
- 서버 팀 : 서버 배포 및 관리에 대한 이론적인 부분 공부 목표
- DB 관리 팀 & 머신러닝 팀 : 데이터베이스와 유사도 검사 기능 잇기 목표

### __4차 회의__ _2022_09_16_
- 9/26 ~ 10/3 매주 월요일 19시 30분에 대면 회의 __예정__
- 이후에는 각자 중간고사 일정 확인 후 대면/비대면 회의 일정 조정 __예정__
- 다음 회의부터는 같이 작업 시작하기 목표
- 기능 구현 팀에서의 생긴 공백 새로 배정  
  박서진 : 인터페이스 활동 일정 안내  
  주시환 : 인터페이스 링크 안내  
  박상욱 : 인터페이스 동아리 방 위치 안내
- 기능 구현 팀 : 각자 맡은 기능 구현 하고, 카카오톡과 연결하기 목표
- 서버팀 : 현재까지 기능 구현 팀에서 완성된 부분을 연결하기 목표
- DB 관리 팀 & 머신러닝 팀 : 현재 완성된 부분에서 심화시키기 목표

### __5차 회의__ _2022_09_26_
- 유사도 검증 기능을 형태소 단위로 분석하여 오타가 들어간 명령어를 받으면 사용자에게 되묻도록 할 __예정__
- 서버를 현재 GCP(구글 클라우드 플랫폼)로 구현되어 있으므로 GCP로 개발하여 연결할 __예정__
- 오라클이 어느 정도 완성도를 갖추면 서버를 오라클로 교체할 __예정__
- 기능 구현 팀에서 현재 카카오톡 챗봇에서 저장된 답변이 나오도록 되어 있지만 답변을 DB에서 가져오기 위해서 DB 관리 팀에 스키마와 쿼리문 요청할 __예정__
- 10/3일 회의는 중간발표일과 겹치므로 중간발표일 일정을 확인 후 디스코드로 진행 여부 결정 __예정__
- 중간 발표 시현을 위해서 각자 기능을 동영상으로 녹화 후 전송 __예정__
- 3일까지 회의 후에는 중간고사 일정 마친 후(31일부터) 회의 일정 조정 __예정__
- "프로젝트 구인/모집" 기능은 "인터페이스 챗봇 도움말" 기능으로 __변경__
- "인터페이스 소개글" 기능의 동아리 관련 정보는 정리해서 전달 __예정__
- 기능 구현 팀 : DB에게 필요한 정보 요청, DB에게서 받은 쿼리문으로 정보 출력해보기
- 서버팀 : SSH 키 생성 후 GCP에 접속하기(접속에 성공했을시 완성된 기능을 서버에서 돌리기) 
- DB 관리 팀 : 기능 구현 팀에서 요청 받은 스키마 구현 후 쿼리문을 작성하여 보내기, 동아리 부원의 이름과 학번이 필요한 부분은 일단 팀원 정보 넣고 테스트 하기
- 머신러닝 팀 : 형태소 분석으로 유사도 검증 기능 구현하기