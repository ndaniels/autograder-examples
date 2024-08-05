
import random
import sys
import math

EPSILON = sys.float_info.epsilon

def triangleArea(a, b, c):
	return (a[0]*b[1] - a[1]*b[0] + a[1]*c[0] \
                - a[0]*c[1] + b[0]*c[1] - c[0]*b[1]) / 2.0;

def cw(a, b, c):
	return triangleArea(a,b,c) < -EPSILON;

def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON;

def collinear(a, b, c):
	return abs(triangleArea(a,b,c)) <= EPSILON

def clockwiseSort(points):
	# get mean x coord, mean y coord
	xavg = sum(p[0] for p in points) / len(points)
	yavg = sum(p[1] for p in points) / len(points)
	angle = lambda p:  ((math.atan2(p[1] - yavg, p[0] - xavg) + 2*math.pi) % (2*math.pi))
	points.sort(key = angle)

def checkHull(hull, points):
	for i in range(0, len(hull) - 2):
		j = i + 1
		p = hull[i]
		q = hull[j]
		pos = 0
		neg = 0
		for r in points:
			if r==p or r == q: continue
			if cw(p,q,r):
				neg += 1
			elif ccw(p,q,r):
				pos += 1
		if (pos == 0 or neg == 0):
			return True
		else:
			return False




def generate(n, min=0, max=2**32-1):
	# min = 0
	# max = 2**32-1
	result = []
	for i in range(n):
		result.append((random.randint(min, max), random.randint(min, max)))
	return result


def random_noncollinear_points(P: int) -> list[tuple[int, int]]:
	"""
	Sample a random set of (P // 4) - 1 points on the (P // 4) x P
	integer lattice such that no three points fall in a line.

	This method is based on Erdos' construction. See https://adamsheffer.wordpress.com/2018/05/31/points-in-general-position/
	additional details. It can be modified to work with any positive integer m
    by only considering values of t for which m and t are relatively prime.

	Parameters
	----------
		P: int - Prime number. Determines the number of points to sample.

	Returns
	-------
		A random set of (P // 4) - 1 points on the (P // 4) x P integer lattice in general position.
	"""
	n = random.randint(1, P - 1)
	return [(t, (n * t ** 2) % P) for t in range(1, P // 4)]
