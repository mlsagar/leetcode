# First Approach Pseudo Code
> Start the pointers at the edge of input. Move them towards each other until they meet.
```
def fn(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left += 1
            2. right -= 1
            3. Both left += 1 and right -= 1
```

# Second Approach Pseudo Code
> Move along both inputs simultaneously until all elements have been checked
```
def fn(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i += 1
            2. j += 1
            3. Both i += 1 and j += 1

    // Step 4: make sure both iterables are exhausted
    // Note that only one of these loops would run
    while i < len(arr1):
        Do some logic here depending on the problem
        i += 1

    while j < len(arr2):
        Do some logic here depending on the problem
        j += 1 
```