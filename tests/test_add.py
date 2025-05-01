from main import add

# 자동빌드 확인
def test_add_positive_numbers():
    assert add(2, 3) == 5