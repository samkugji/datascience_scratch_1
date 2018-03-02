def vector_add(v, w):
    """각 성분끼리 더한다."""
    return [v_i + w_i for v_i, w_i in zip(v, w)]
    

def vector_subtract(v, w):
    """각 성분끼리 뺀다."""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """모든 벡터의 각 성분들끼리 더한다."""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def vector_sum(vectors):
    from functools import reduce
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c는 숫자, v는 벡터"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """i번째 성분이 입력된 벡터의 i번째 성분의 평균을
    의미하는 벡터를 계산해준다."""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1*w_1 + v_2*w_2 + ..."""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1*v_1 + v_2*v_2 + ... + v_n*v_n"""
    return dot(v, v)

def magnitude(v):
    import math
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1-w_1)**2 + ... + (v_n - w_n)**2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    import math
    return math.sqrt(squared_distance(v, w))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 ## A의 첫번째 행의 element의 갯수
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_columns(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """(i, j)번째 원소가 entry_fn(i, j)인 
    num_rows x num_cols list를 반환"""
    return [[entry_fn(i, j) 
             for j in range(num_cols)]
             for i in range(num_rows)]

def is_diagonal(i, j):
    """대각선의 원소는 1, 나머지 원소는 0"""
    return 1 if i == j else 0