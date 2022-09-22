lst = [1,2,3,4,5]
it = iter(lst)

print(next(it))
print(next(it))
print(next(it))

def custome_for(iterable, func):
    it = iter(iterable)
    while True:

        try:
            print(next(it))
        except StopIteration:
            print("End of loop")
            return



custome_for(lst,print)

