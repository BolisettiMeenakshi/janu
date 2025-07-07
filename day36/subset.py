arr = [3, 1, 2]
def fun(index, subset):
    if index == len(arr):
        print(subset)
        return
    subset.append(arr[index])
    fun(index + 1, subset)
    subset.pop()
    fun(index + 1, subset)
fun(0, [])