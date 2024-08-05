#!/usr/bin/python
import unittest
import hashlib
import os
import sys
import subprocess
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

import convex_hull
import goodhull



class TestHull(unittest.TestCase):
	@weight(5)
	def testTriangle(self):
		'''Test on a triangle'''
		a = (10, 10)
		b = (20, 60)
		c = (5, 100)
		points = [a, b, c]
		studentHull = convex_hull.compute_hull(points)
		self.assertTrue(goodhull.checkHull(studentHull, points))
		self.assertTrue(len(studentHull) == 3)

	@weight(5)
	def testQuadrilateral(self):
		'''Test on a quadrilateral with one interior point'''
		a = (10, 10)
		b = (20, 60)
		c = (5, 100)
		d = (15, 60)
		points = [a, b, c, d]
		studentHull = convex_hull.compute_hull(points)
		self.assertTrue(goodhull.checkHull(studentHull, points))
		self.assertTrue(len(studentHull) == 3)

	@weight(10)
	def testRandomTen(self):
		'''Test on 10 random points in a small space'''
		points = goodhull.random_noncollinear_points(40)
		# points = goodhull.generate(10, 0, 1000)
		studentHull = convex_hull.compute_hull(points)
		self.assertTrue(goodhull.checkHull(studentHull, points))

	@weight(10)
	def testRandomThousand(self):
		'''Test on 1000 random points in a moderate space'''
		# points = goodhull.generate(1000, 0, 10000)
		points = goodhull.random_noncollinear_points(4000)
		studentHull = convex_hull.compute_hull(points)
		self.assertTrue(goodhull.checkHull(studentHull, points))

	@weight(20)
	def testRandomMillion(self):
		'''Test on 1000000 random points in a large space'''
		# too many problems with minor differences between solutions... FP error?
		# points = goodhull.generate(1000000, 0, 100000000)
		points = goodhull.random_noncollinear_points(4000000)
		studentHull = convex_hull.compute_hull(points)
		self.assertTrue(goodhull.checkHull(studentHull, points))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHull)
    JSONTestRunner().run(suite)
