from utils import arrs


from utils.arrs import get

def get(arr, index, default):
    if index < len(arr):
        return arr[index]
    else:
        return default


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


