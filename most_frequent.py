def most_frequent(l1):
    """ returns the most frequent element in l1.
    :param l1: List[Any] -- the large python list

    Required runtime: Expected O(N) where N is len(l1)

    return: Any -- the most frequent element
    """
    # To do
    dic = {}
    for i in l1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    m = dic[l1[0]]
    res = l1[0]
    for i in dic:
        if dic[i] > m:
            m = dic[i]
            res = i
    return res
        

def main():
    l1 = [1,2,3,4,5,6,7,8,9,0,0]
    print(most_frequent(l1), "should be 0")
    l2 = ['aaa', 'bbb', 'ccc', 'ddd', 'a', 'aaa']
    print(most_frequent(l2), "should be aaa")
    l3 = [5, 9, 5, 2, 9, 9, 8, 12, 6, 2, 11, 19, 0, 15, 0, 14, 14, 8, 11, 14, 14, 5, 9, 14, 15, 7, 12, 7, 10, 16, 7, 20, 4, 15, 0, 19, 19, 7, 7, 16, 2, 3, 20, 1, 3, 3, 4, 14, 6, 4, 12, 13, 14, 13, 2, 19, 1, 15, 18, 0, 17, 7, 18, 16, 14, 10, 1, 13, 18, 11, 1, 17, 16, 20, 0, 12, 4, 1, 0, 15, 5, 11, 14, 17, 12, 3, 13, 0, 16, 16, 3, 3, 8, 3, 20, 0, 4, 3, 5, 15]
    print(most_frequent(l3), "should be 14")

if __name__ == '__main__':
    main()

