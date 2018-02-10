def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    "균등 분포를 따르는 확률변수의 값이 x보다 작거나 같을 확률을 반환"
    if x < 0 : return 0
    elif x < 1 : return x
    else: return 1
    
def normal_pdf(x, mu = 0, sigma = 1):
    import math
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2 / 2 / sigma**2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0,sigma=1):
    import math
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """이진 검색 알고리즘을 사용해서 역함수 근사"""
    
    # 표준정규분포가 아니라면 표준정규분포로 변환
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0            # normal_cdf(-10)는 0에 근접
    hi_z,  hi_p  =  10.0, 1            # normal_cdf(10)는 1에 근접
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # 중간 값
        mid_p = normal_cdf(mid_z)      # 중간 값의 누적분포 값을 계산
        if mid_p < p:
            # 중간 값이 너무 작다면 더 큰 값들을 검색
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # 중간 값이 너무 크다면, 더 작은 값들을 검색
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

def bernoulli_trial(p):
    import random
    return 1 if random.random() < p else 0

def binomial(p, n):
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):
    import matplotlib.pyplot as plt
    from collections import Counter
    import math
    
    data = [binomial(p, n) for _ in range(num_points)]
    
    # 이항분포를 막대그래프로 표현s
    histogram = Counter(data)  # 빈도수 세기
    plt.figure(figsize = (10, 5))
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8, color = 'grey', label = 'binomial')
    
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 근사된 정규 분포 
    xs = range(min(data), max(data) + 1)
    ys = [normal_pdf(i, mu, sigma) for i in xs]
    plt.plot(xs,ys, label = 'norm')
    plt.legend()
    plt.show()