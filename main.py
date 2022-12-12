def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

    """
How does this solution ensure data immutability?
Immutable data types are those, whose values cannot be modified once they are created.


Is this solution a pure function? Why or why not?
Yes. It's defini as a function def.


Is this solution a higher order function? Why or why not?
This isn't Higher Order Function if it contains other functions as a parameter or returns a function as an output.

Would it have been easier to solve this problem using a different programming style?
NO

Why in particular is functional programming a helpful paradigm when solving this problem?
Functions produce the same output as the given input, this means they aren't any changes or any other hidden output produced
    """