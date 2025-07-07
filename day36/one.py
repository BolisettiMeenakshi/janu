def fun(count,end):
    if count == end:
        return
    print(count)
    count -= 1
    fun(count,end)
fun(4,0)