import random
import time

def swap(l, i, j):
    """交换两元素的位置"""
    l[i], l[j] = l[j], l[i]

def is_Sorted(l):
    """是否已排序"""
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def test_Sort(l, sortName):
    """测试排序性能"""
    start_time = time.time()
    sortName(l)
    cost_time = time.time() - start_time
    return "is_Sorted: %s,cost_time:%s" % (is_Sorted(l), cost_time)

def generate_random_list(n, rangeL, rangeR):
    """生成排序测试用例"""
    if rangeL > rangeR:
        raise ValueError("Illegal input!!!")
    l = []
    for i in range(n):
        l.append(random.randint(rangeL, rangeR))
    return l

def selectionSort(l):
    """选择排序"""
    for i in range(len(l)):
        minIndex = i
        for j in range(i+1, len(l)):
            if l[j] < l[minIndex]:
                minIndex = j
        l[i], l[minIndex] = l[minIndex], l[i]
    return l

def insertionSort(l):
    """插入排序"""
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break
    return l

def insertionSortDB(l):
    """插入排序改进"""
    for i in range(1 ,len(l)):
        e = l[i]
        j = i
        while j > 0 and l[j - 1] > e:
            l[j] = l[j -1]
            j -= 1
        l[j] = e
    return l

def bubbleSort(l):
    """冒泡排序"""
    is_exchange = False
    for i in range(len(l) - 1, 0 ,-1): #次数
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                is_exchange = True
        if not is_exchange:
            break
    return l

def shellSort(l):
    """希尔排序"""
    gap = len(l) // 2
    while gap > 0:
        for start_pos in range(gap):
            gapInsertionSort(l, start_pos, gap)
        gap = gap // 2
    return l

def gapInsertionSort(l, start_pos, gap):
    """希尔排序实现函数"""
    for i in range(start_pos + gap, len(l), gap):
        position = i
        current_value = l[i]
        #插入排序
        while position >= gap and l[position - gap] > current_value:
            l[i] = l[i - gap]
            position = position - gap
        l[position] = current_value


if __name__ == "__main__":
    n = 1000
    l1 = generate_random_list(n,0,n)
    l2 = l1[:]
    l3 = l1[:]
    l4 = l1[:]
    res1 = test_Sort(l1, selectionSort)
    res2 = test_Sort(l2, insertionSort)
    res3 = test_Sort(l3, insertionSortDB)
    res4 = test_Sort(l4, bubbleSort)

    print(res1)
    print(res2)
    print(res3)
    print(res4)

