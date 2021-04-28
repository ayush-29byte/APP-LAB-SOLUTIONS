import multiprocessing
import time


def square(x):
	return x * x


if __name__ == '__main__':
	pool = multiprocessing.Pool()
	result_async = [pool.apply_async(square, args = (i, )) for i in
					range(10)]
	results = [r.get() for r in result_async]
	print("Output: {}".format(results))
#CODE BY AYUSH SAXENA