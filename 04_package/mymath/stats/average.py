def data_mean(data):
    return sum(data) / len(data)

# 데이터의 중앙값을 구해 주는 함수
def data_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        # 데이터 개수가 짝수라면 중앙값 두 개의 평균을 반환
        # [a, b, c, d, e, f] -> median = (c + d) / 2
        return (data[n / 2] + data[ (n / 2) - 1]) / 2
    else:
        # [a, b, c, d, e] -> median = c
        return data[ (n - 1) / 2]