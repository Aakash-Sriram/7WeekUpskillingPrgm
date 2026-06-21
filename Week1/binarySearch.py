class Bs:
    def __init__(self, arr):
        self.arr = arr
    def doBS(self,target):
        low =0
        high = len(self.arr)-1
        while low<=high:
            mid = low + (high-low)//2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
arr = list(map(int, input().split()))
target = int(input("Target? "))
bs = Bs(sorted(arr))
print(bs.doBS(target))  