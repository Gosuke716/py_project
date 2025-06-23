import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# StudentScoreAnalysis 클래스 정의 
class StudentScoreAnalysis:
    # 생성자
    def __init__(self):
        # 학생 이름 생성(학생1 ~ 학생20)
        self.students = [f'학생{i}' for i in range(1, 21)]
        
        # 과목 성적 난수 생성 (50~100) 및 20명의 점수를 생성
        scores = {
            '이름': self.students,
            '수학': np.random.randint(50, 101, size=20),
            '영어': np.random.randint(50, 101, size=20),
            '과학': np.random.randint(50, 101, size=20)
        }
        
        # 데이터프레임 생성
        self.df = pd.DataFrame(scores)

    # 과목별 평균 점수 막대 그래프 시각화 함수
    def plot_average(self):
        # 과목별 평균 계산
        subject_means = self.df[['수학', '영어', '과학']].mean()

        # 시각화
        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(10, 5))
        plt.bar(subject_means.index, subject_means.values, color='blue')
        plt.title('과목별 평균 점수')
        plt.ylabel('평균 점수')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

    # 평균 성적 상위 5명 막대 그래프 시각화 함수
    def plot_top5(self):
        # 학생별 평균 점수 계산
        self.df['평균'] = self.df[['수학', '영어', '과학']].mean(axis=1)
        
        # 평균 성적 상위 5명 추출
        top5 = self.df.sort_values(by='평균', ascending=False).head(5)

        # 시각화
        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(10, 5))
        plt.bar(top5['이름'], top5['평균'], color='red')
        plt.title('평균 성적 상위 5명')
        plt.ylabel('평균 점수')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()


# 실행 예시
if __name__ == "__main__":
    analysis = StudentScoreAnalysis()
    analysis.plot_average()
    analysis.plot_top5()
