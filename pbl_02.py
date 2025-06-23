import re
import csv
import os
from collections import Counter

class IPLogAnalyze:
    # 생성자 
    def __init__(self, file_path):
        self.file_path = file_path
        #Counter 사용
        self.ip_counter = Counter()

    #IP 주소 추출 함수
    def extract_ip(self):
        # ip 주소
        # 숫자1~3자리. 숫자 1~3자리 숫자 1~3 자리.숫자 1~3자리 형식
        # 패턴 : 숫자 1~3 자리 + . 3번 반복, 마지막은 숫자 1~3자리로 마무리
        # \b로 단어 처리
        # (?:\d{1,3}\.){3} 로 세번 반복표현
        # 마지막 \d{1,3} 처리
        ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

        # 파일이 존재하지 않는다면 존재하지 않는다는 메시지 출력 (파일 존재 여부 확인)
        if not os.path.exists(self.file_path):
            print(f"{self.file_path} 파일이 존재하지 않습니다")

        try:
            # 파일 utf-8 형식으로 열기
            with open(self.file_path, 'r', encoding='utf-8') as file:
                # 한줄씩 읽기
                for line in file:
                    # 각 줄에서 정규식으로 line(IP) 추출
                    match = ip_pattern.search(line)
                    if match:
                        # 추출 IP의 카운트 누적
                        ip = match.group()
                        # Counter
                        self.ip_counter[ip] += 1
        # 파일 처리 오류시 예외 처리
        except Exception as e:
            print(f"파일 처리 중 오류 발생: {e}")
           

    # 상위 3개 IP 주소 출력하는 함수
    def print_top3_ip(self, n=3): # 3개 출력 말고 더 많이 출력하려면 n 수정
        print(f"\n상위 {n}개 접속 IP:")
        # most_common 함수로 접속 횟수 많은 순으로 반환
        for ip, count in self.ip_counter.most_common(n):
            print(f"{ip} : {count}회")

    # 분석 결과 CSV 파일로 저장하는 함수
    def save_to_csv(self, output_file='ip_analysis.csv'):
        try:
            #파일 쓰기 형식으로 열기 utf-8-sig 인코딩으로 csv 모듈로 저장
            with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['IP 주소', '접속 횟수'])
                # 횟수 많은 순으로 작성
                for ip, count in self.ip_counter.most_common():
                    writer.writerow([ip, count])
        # CSV 저장 중 오류 발생시 예외처리
        except Exception as e:
            print(f"CSV 저장 중 오류 발생: {e}")


# 실행
if __name__ == "__main__":
    #로그 파일 경로 입력 받기
    #20250613_091920_sample_log_file.log
    file_path = input("분석할 로그 파일 경로를 입력하세요: ").strip()

    analyzer = IPLogAnalyze(file_path)
    
    analyzer.extract_ip() # IP 추출 성공시
    analyzer.print_top3_ip() # 상위 3개 IP를 출력하고
    analyzer.save_to_csv() #CSV 파일로 결과 저장
