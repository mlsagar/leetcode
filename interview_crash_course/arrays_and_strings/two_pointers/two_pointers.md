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