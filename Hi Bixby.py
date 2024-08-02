import speech_recognition as sr
import pyttsx3

# respond 함수 정의
def respond():
    message = "챗봇이 하는 응답"
    engine.say(message)
    engine.runAndWait()
    print("엄마")



# 음성 엔진 초기화
engine = pyttsx3.init()
# 음성 속성 설정 (옵션)
engine.setProperty('rate', 150)  # 음성 속도 (기본값은 200)
engine.setProperty('volume', 1.0)  # 볼륨 (기본값은 1.0, 0.0에서 1.0 사이)


# 음성 인식기 객체 생성
recognizer = sr.Recognizer()

# 마이크 사용 설정
with sr.Microphone() as source:
    print("음성을 입력하세요...")

    # 주변 소음을 반영하여 음성 인식기 초기화
    recognizer.adjust_for_ambient_noise(source)
    
    try:
        while True:
            print("듣고 있습니다...")
            # 음성 입력 받기
            audio = recognizer.listen(source)
            
            # 음성 텍스트 변환
            try:
                text = recognizer.recognize_google(audio, language="ko-KR")
                print(f"인식된 텍스트: {text}")

                # 특정 단어 "쓰레기통" 감지
                if "쓰레기통" in text:
                    respond()
            
            except sr.UnknownValueError:
                print("음성을 이해할 수 없습니다.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition 서비스에 요청할 수 없습니다; {e}")

    except KeyboardInterrupt:
        print("프로그램이 종료되었습니다.")
