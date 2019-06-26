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

def mergeSort(l, left, right):
    """归并排序"""
    _mergeSort(l, left, right)

def _merge(l, left, mid, right):
    aux = [0] * (right + 1 -left)
    for i in range(left, right + 1):
        aux[i - left] = l[i]
    i = left
    j = mid + 1
    for k in range(left, right +1):
        # 一个子数组比较完后为空
        if i > mid:
            l[k] = aux[j - left]
            j += 1
        elif j > right:
            l[k] = aux[i - left]
            i += 1
        # 两子数组元素比较
        elif aux[i - left] < aux[j - left]:
            l[k] = aux[i - left]
            i += 1
        else:
            l[k] = aux[j - left]
            j += 1

def _mergeSort(l, left, right):

    if left >= right:
        return
    # if (right - left) <= 16:  #优化2：限定数组元素个数，决定排序算法
    #     insertionSortDB(l, left, right)
    # else:
    mid = (left + right) // 2
    _mergeSort(l, left, mid)
    _mergeSort(l, mid + 1, right)

    if l[mid] > l[mid + 1]:  # 优化1：若子数组是按照顺序排列时，则不进行排序合并
        _merge(l, left, mid, right)

def mergeSortBU(l):
    for size in range(1, len(l)):
        pass



if __name__ == "__main__":
    n = 21000
    l1 = generate_random_list(n, 0, n)
    l2 = l1[:]

    res1 = test_Sort(l1, insertionSortDB, left = 0, right = n - 1)
    res2 = test_Sort(l2, mergeSort, left = 0, right = n - 1)

    print(res1)
    print(res2)