import random,time

def is_Sorted(l):
    """是否已排序"""
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def test_Sort(l, sortName, left, right):
    """测试排序性能"""
    start_time = time.time()
    sortName(l,left,right)
    cost_time = time.time() - start_time
    print(l)
    return "is_Sorted: %s,cost_time:%s" % (is_Sorted(l), cost_time)

def generate_random_list(n, rangeL, rangeR):
    """生成排序测试用例"""
    if rangeL > rangeR:
        raise ValueError("Illegal input!!!")
    l = []
    for i in range(n):
        l.append(random.randint(rangeL, rangeR))
    return l

def swap(l, i, j):
    """交换两元素的位置"""
    l[i], l[j] = l[j], l[i]

def insertionSortDB(l, left, right):
    """插入排序改进"""
    for i in range(left + 1, right + 1):
        e = l[i]
        j = i
        while j > 0 and l[j - 1] > e:
            l[j] = l[j -1]
            j -= 1
        l[j] = e
    return l

def quickSort(l, left, right):
    """快速排序"""
    _quickSort(l, left, right)

def _quickSort(l, left, right):
    if (right - left) < 15:
        insertionSortDB(l, left, right)   #优化1
        return
    p = _partition(l, left, right)
    _quickSort(l, left, p-1)
    _quickSort(l, p + 1, right)

def _partition(l, left, right):
    """
    对l[left,right]部分进行partition操作
    返回p,使得l[left..p-1] < l[p];l[p+1..right] > l[p]
    """
    #优化2：解决快速排序最差n^2时间复杂度，随机化取基准值
    swap(l, left, random.randint(left, right))

    v = l[left] #默认设定左侧基准值
    # l[l+1..j] < v;l[j+1..i] >v
    j = left
    i = left + 1
    while i <= right:
        if l[i] <  v:
            swap(l, j+1, i)
            j += 1
        i += 1
    swap(l, left, j)

    return j

if __name__ == "__main__":
    n = 20000
    l1 = generate_random_list(n, 0, n)
    res1 = test_Sort(l1, quickSort, left = 0, right = n - 1)
    print(res1)