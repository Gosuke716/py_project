import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SalesAnalysis 클래스 정의
class SalesAnalysis:
    #생성자
    def __init__(self):
        # 2024년 1월 ~ 12월 까지의 날짜 pd.date_range로 날짜 생성
        self.dates = pd.date_range(start='2024-01-01', end='2024-12-31')
        
        # 일별 매출 데이터 생성 (1000 ~ 10000 사이 난수)
        sales = np.random.randint(1000, 10001, size=len(self.dates))
        
        # 데이터프레임 생성 (컬럼: 날짜, 매출)
        self.data = pd.DataFrame({
            'Date': self.dates,
            'Sales': sales
        })
    # 월별 매출 계산 메서드
    def monthly_sales(self):
        # 일까지 포함된 날짜를 월단위로 표시
        self.data['Month'] = self.data['Date'].dt.to_period('M')
        # 각 월 기준 매출 합산(groupby 활용)
        monthly_sales = self.data.groupby('Month')['Sales'].sum()
        # 월 매출 반환
        return monthly_sales

    # 월별 매출 시각화 메서드
    def plot_monthly_sales(self, monthly_sales):
        # 한글 폰트 설정 (맑은 고딕체)
        plt.rc('font', family='Malgun Gothic')
        # 그래프 크기는 10, 5 사이즈로 지정
        plt.figure(figsize=(10, 5))
        # 선그래프로 표현 선위에 마커 표시
        monthly_sales.plot(marker='o')
        # 타이틀, 라벨이름,배경 격자 추가
        plt.title('2024년 월별 매출 추이')
        plt.xlabel('월')
        plt.ylabel('매출')
        plt.grid(True)
        # 그래프 표시
        plt.show()

# 실행
if __name__ == "__main__":
    analysis = SalesAnalysis()
    monthly_sales = analysis.monthly_sales()
    analysis.plot_monthly_sales(monthly_sales)
