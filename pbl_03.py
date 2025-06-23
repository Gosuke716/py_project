import os
import time
import re

# 감시 클래스 생성
class Monitor:
    # 생성자
    # 파일 경로 ./monitor_directory
    # 감시주기(interval) : 5초 단위로 감시
    def __init__(self, path='./monitor_directory', interval=5):
        self.path = path # 경로
        self.interval = interval # 주기
        self.files = set() # 감지파일 집합(set) 로 저장

        # 파일경로가 존재하지 않을시 
        # if not os.path.exists(self.path):
        #     os.makedirs(self.path) # 디렉토리 만들기
        #     print(f'{self.path} 파일 경로가 존재하지 않습니다')

        # 경로에 있는 모든 파일을 읽어서 files 에 저장
        self.files = set(os.listdir(self.path))
        # 감지된 파일 개수 출력(파일 초기 목록 기록)
        print(f'{len(self.files)}개 파일 감지됨.')

    # 주요 정보(주석, 이메일, sql문) 탐지 함수
    def detect(self, file_path):
        # 정규화 패턴 딕셔너리로 정의
        patterns = {
            '이메일 주소': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            '주석': r'#.*|//.*|/\*.*?\*/',
            'SQL문': r'\b(SELECT|INSERT|UPDATE|DELETE|DROP|FROM|WHERE)\b'
        }

        try:
            # 읽기모드로 파일 열기
            # utf-8 인코딩, errors = 'ignore'로 인코딩 문제 발생 무시
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # 패턴별로 정규식 검색 수행
                for label, pattern in patterns.items():
                    matches = re.findall(pattern, content)
                    if matches:
                        # 민감정보 발생 건수 출력
                        print(f'민감 정보 - {label}: {len(matches)}건 탐지되었습니다')
                        # 민감정보 출력
                        for match in matches[:]:
                            print(f'민감정보: {match.strip()[:]}')
        #파일 내용 읽기 실패하였을 때 예외처리
        except Exception as e:
            print(f'{file_path}파일 내용 읽기 실패: {e}')
    
    # 초기 디렉토리 탐색 이후
    # 사용자가 멈출때까지 디렉토리 감시하는 메서드
    # 사용종료는 CTRL + C 로 종료
    def monitor(self):
        print('디렉터리 감시를 시작합니다 종료하려면 Ctrl+C를 눌러주세요.')
        try:
            # 멈출때까지 무한반복
            while True:
                # 현재 디렉토리 파일 목록 읽기
                current_files = set(os.listdir(self.path))
                # 기존 목록과 비교해서 새로운 파일 집합 계산하기 (개수 출력을 위함)
                new_files = current_files - self.files

                # 현재 디렉토리 파일 목록과 기존목록을 비교해서 새로운 파일 집합 계산
                for file in new_files:
                    file_path = os.path.join(self.path, file)
                    print(f'\n새 파일 발견: {file}')

                    # 확장자 체크후 주의 파일로 분류 및 알림
                    extension = os.path.splitext(file)[1].lower()
                    if extension in ['.py', '.js', '.class']:
                        print(f'주의 파일 감지됨 - {file}')

                    # 주요정보 탐지 메서드 실행 (1 싸이클)
                    self.detect(file_path)
                # 현재 파일 목록 갱신, 5초 인터벌 시간 대기
                self.files = current_files
                time.sleep(self.interval)
        # 사용자가 ctrl + c 누를때 종료시키기
        except KeyboardInterrupt:
            print('\n모니터링을 중지합니다.')

# 실행
if __name__ == "__main__":
    monitor = Monitor()
    monitor.monitor()
