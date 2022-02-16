import numpy as np

if __name__=='__main__':
    arr = np.array([[1,2,3]])
    brr = np.array([[10],[20],[40]])

    print('arr.shape: {}'.format(arr.shape))
    print('brr.shape: {}'.format(brr.shape))
    print('arr @ brr: {}'.format(np.dot(arr, brr)))
    print('arr * brr: {}'.format(np.multiply(arr, brr)))
    