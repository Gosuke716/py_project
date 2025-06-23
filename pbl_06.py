import pandas as pd
import matplotlib.pyplot as plt

# CustomerSalesAnalysis 클래스 생성
class CustomerSalesAnalysis:
    # 생성자(데이터는 아래 샘플 데이터로 받기)
    def __init__(self, data: pd.DataFrame):
        self.df = data
        # 구매일자를 datetime 날짜 포맷으로 변환
        self.df['구매일자'] = pd.to_datetime(self.df['구매일자'])
        # 총매출을 수량 * 단가로 파생열 생성
        self.df['총매출'] = self.df['수량'] * self.df['단가']
        # 구매일자에서 월을 추출해서 열 생성
        self.df['월'] = self.df['구매일자'].dt.month

    # 월별 매출을 막대 그래프로 시각화하는 함수
    def plot_monthly_sales(self):
        # 한글 폰트
        plt.rc('font', family='Malgun Gothic')
        # 월 별로 그룹화 하여 총매출을 합산하고 시계열로 정렬
        monthly_sales = self.df.groupby('월')['총매출'].sum().sort_index()
        # 막대그래프 시각화 
        monthly_sales.plot(
            kind='bar', 
            figsize=(10, 5), 
            color='blue')
        plt.rc('font', family='Malgun Gothic')
        plt.title('월별 매출 총합')
        plt.xlabel('월')
        plt.xticks(rotation = 0)
        plt.ylabel('총매출')
        plt.show()

    # 고객별 누적 매출을 파이차트로 시각화하는 함수
    def plot_customer_contribution(self):
        # 한글 폰트
        plt.rc('font', family='Malgun Gothic')
        # 고객별로 그룹화 하여 총매출을 합산
        customer_sales = self.df.groupby('고객명')['총매출'].sum()
        # 파이차트 시각화 (autopct는 소수점 첫째자리까지)
        customer_sales.plot(kind='pie', 
                            autopct='%.1f',
                            figsize=(10, 5))
        plt.title('고객별 누적 매출')
        plt.ylabel('')
        plt.show()

# 실행
if __name__ == "__main__":
    # 샘플 데이터
    sample_data = pd.DataFrame({
        '고객명': ['손흥민', '이강인', '박지성', '김민재', '이강인', '차범근', '손흥민'],
        '구매일자': ['2025-01-25', '2025-02-01', '2025-03-15', '2025-04-25', '2025-05-05', '2025-06-14', '2025-06-15'],
        '상품명': ['축구화', '유니폼', '축구공', '축구화', '트레이닝 바지', '축구공', '양말'],
        '수량': [1, 2, 2, 3, 5, 1, 5],
        '단가': [100000, 150000, 50000, 100000, 12000, 50000, 3000]
    })

    analysis = CustomerSalesAnalysis(sample_data)
    analysis.plot_monthly_sales()
    analysis.plot_customer_contribution()
