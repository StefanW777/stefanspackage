from stefanspackage import myFunction

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """

    assert myFunction.bubble_sort(np.array([8, 34, 2, 71, 14, 30])) == array([2, 8, 14, 30, 34, 71])
    assert myFunction.bubble_sort(np.array([10, 1, 12, 9, 2])) ==array([1, 2, 9, 10, 12])
    assert myFunction.bubble_sort(np.array([77, 3, 11, 5])) == array([3, 5, 11, 77])










    assert myFunction.quick_sort([1,3,66,7,5,23,17])
    assert myFunction.quick_sort([88,26,16,75,45])
    assert myFunction.quick_sort([-9, 7, 4, 1, -1, -99])
