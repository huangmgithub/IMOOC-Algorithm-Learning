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

def quick3WaySort(l, left, right):
    """双路快速排序"""
    _quickSort3(l, left, right)

def _quickSort3(l, left, right):
    """
    三路快速排序处理 l[left..right]
    将l[left..right] < v; == v; > v 分成三部分
    之后递归 < v; > v两部分继续三路快速排序
    """
    if (right - left) <= 15:
        insertionSortDB(l, left, right)   #优化1
        return

    # partition
    # 优化2：解决快速排序最差n^2时间复杂度，随机化取基准值
    swap(l, left, random.randint(left, right))
    v = l[left]  # 默认设定左侧基准值

    lt = left  # l[left+1..lt] < v
    gt = right + 1 #l[gt..right] > v
    i = left + 1  #l[lt+1..i) == v
    while i < gt:
        if l[i] < v:
            swap(l, lt + 1, i)
            lt += 1
            i += 1
        elif l[i] > v:
            swap(l,gt - 1,i)
            gt -= 1
        else:
             i += 1

    swap(l, left, lt)
    _quickSort3(l, left, lt-1)
    _quickSort3(l, gt, right)


if __name__ == "__main__":
    n = 20000
    l1 = generate_random_list(n, 0, n)
    res1 = test_Sort(l1, quick3WaySort, left = 0, right = n - 1)
    print(res1)