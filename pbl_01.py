#StudentScores 클래스 정의
class StudentScores:
    # 생성자: 파일을 읽고 데이터를 딕셔너리에 저장
    def __init__(self, filename):
        self.filename = filename
        self.scores = {}
        try:
            # 파일 읽기 인코딩 방식은 utf-8로 지정
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip() # 공백 문자 제거
                    if not line: # 비어있는 줄에 대비해서 다음줄로 넘어가기
                        continue
                    try:
                        name, score = line.split(',') # 이름과 점수를 , 로 구분
                        self.scores[name] = int(score) # 정수형으로 반환
                    # 이름과 점수에 해당하지 않는 잘못된 데이터 형식 무시
                    except ValueError: 
                        print(f"{line}은 잘못된 데이터 형식입니다.")
        #FileNotFoundError 예외처리
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {self.filename}")
        # 파일 읽기 중 오류발생 할때 띄울 예외처리
        except Exception as e:
            print(f"파일 읽기 중 오류 발생: {e}")

    # 평균 점수 계산 메서드
    def calculate_average(self):
        return sum(self.scores.values()) / len(self.scores)

    # 평균 이상 이름 리스트 반환 메서드
    def get_above_average(self):
        avg = self.calculate_average()
        return [name for name, score in self.scores.items() if score >= avg]

    # 평균 미만 학생을 파일로 저장하는 메서드
    def save_below_average(self):
        avg = self.calculate_average()
        try:
            #쓰기 모드로 열기
            with open('below_average_korean.txt', 'w', encoding='utf-8') as file:
                for name, score in self.scores.items():
                    if score < avg:
                        file.write(f"{name},{score}\n")
        # 파일 저장 오류 발생할 때 띄울 예외처리
        except Exception as e: 
            print(f"파일 저장 중 오류 발생: {e}")

    # 평균 점수와 평균 이상 학생 리스트 출력 메서드
    def print_summary(self):
        avg = self.calculate_average()
        print(f"평균 점수: {avg}")
        above_avg_students = self.get_above_average()
        print("평균 이상 학생:")
        for student in above_avg_students:
            print(f"{student} ({self.scores[student]})")


# 실행
if __name__ == "__main__":
    student_scores = StudentScores('scores_korean.txt')
    student_scores.print_summary()
    student_scores.save_below_average()

