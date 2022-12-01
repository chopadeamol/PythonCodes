# Extended Assignment Operators

alpha = [1,2,3]
beta = alpha        # an alias for alpha
beta += [4,5]       # extends the original list two more elements
beta = beta + [6,7] #reassigns beta to a new list [1,2,3,4,5,6,7]
print(alpha)        # will be [1,2,3,4,5]


# d[key]              value associated with given key
# d[key] = value      set (or reset) the value associted with given key
# del d[key]          remove key and its associted value from dictionary
# key in d            containment check
# key not in d        non-containment check
# d1 == d2            d1 is equivalent to d2
# d1 != d2            d1 is not equivalent to d2