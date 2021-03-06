#-*- coding: utf-8 -*-
#utf-8로 인코딩
from flask import Flask

app = Flask(__name__)  #객체 생성
#Flask 클래스 인자
#import_name 애플리케이션 패키지의 이름을 지정하는 인자. 문자열로 정의. 인스턴스를 생성할 때 꼭 필요한 인자
#static_url_path static_folder를 웹에서 접근할 때 어떤 경로를 사용할 것인지 지정. 문자열
#static_folder 프로그램 소스 트리에서 정적파일을 서비스하는 폴더명을 지정. 문자열
#template_folder 프로그램 소스트리에서 뷰 함수가 사용할 HTML파일이 위치하는 폴더명을 지정. 문자열

@app.route('/')  #root에 라우팅, 라우팅 할 URI를 요청했을 때 호출 될 함수를 바로 아래 작성하면 됨
def hello_flask():  #특정 URL을 호출했을 때 호출되는 함수 정의, 뷰 함수라고 함
    return 'Hello Flask!'

if __name__ == '__main__':  #실행되는 모듈이 파이썬 인터프리터에 의해 메인 모듈로 실행됐는지 임포트되어 사용됐는지 확인하여
    app.run()               #메인 모듈로 실행됐으면 테스토 용도로 사용되는 로컬 서버인 run()함수를 실행한다.