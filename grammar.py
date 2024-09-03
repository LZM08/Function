#중첩 함수 (Nested function)
# 함수 내부에 정의된 또 다른 함수
# 중첩함수는 해당 함수가 정의된 함수 내에서 호출 및 반환 가능
# 함수 안에 선언된 변수는 함수 안에서만 사용 가능한 원리와 동일 (로컬 변수)

#First-class 함수 
# 다음과 같이 다룰 수 있는 함수를 First-class 함수라고 부름
# 함수 자체를 변수에 저장 가능
# 함수의 인자에 다른 함수를 인수로 전달 가능
# 함수의 반환 값(return 값)으로 함수를 전달 가능


# 필요한 라이브러리 가져오기
import requests  # 웹 페이지 요청을 위해 사용
from bs4 import BeautifulSoup  # HTML 파싱을 위해 사용

#웹 페이지 가져오기
res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')  
link_titles = soup.select("ul#hobby_course_list > li")  # ul 태그의 ID가 'hobby_course_list'인 요소의 li 자식 요소들을 선택

#선택된 요소들에서 텍스트만 추출하여 리스트에 저장
data = list()  
for link_title in link_titles:  # link_titles 리스트에 포함된 각 li 요소에 대해 반복
    data.append(link_title.get_text())  # li 요소에서 텍스트를 추출해 data 리스트에 추가


def list_creator(tag):  
    def text_wrapper(list_data):  
        for item in list_data:  # 리스트 데이터에 있는 각 항목에 대해 반복
            print('{0} {1}'.format(tag, item))  
    return text_wrapper  


data_list_minus = list_creator('-')  
data_list_minus(data)
