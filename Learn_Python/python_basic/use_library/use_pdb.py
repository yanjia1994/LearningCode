import pdb


def combine(s1, s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 + '"'   # encloses it in double quotes,...
    return s3            # and returns it.


if __name__ == '__main__':
    a = "aaa"
    b = "bbb"
    c = "ccc"

    pdb.set_trace()

    my_list = [0, 1]
    final = combine(a, b)
    print(final)
