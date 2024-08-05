#!/usr/bin/python
import unittest
import hashlib
import os
import sys
import subprocess
import array
from gradescope_utils.autograder_utils.decorators import weight, leaderboard, visibility
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import util

# here we will run the tests just for functional correctness
huffman_impl = util.getProgram()

class TestHuffman(unittest.TestCase):

    @visibility('visible')
    @weight(20)
    def testLongTextInput(self):
        """Test on Long Text Input, correct and effective compression"""
        # verify the compression is smaller, and the files the same
        infile = 'longtext.txt'
        midfile = 'midfile'
        outfile = 'longtext_out.txt'
        exe = subprocess.Popen(f"{huffman_impl} -c {infile} {midfile}", shell=True)
        exe.wait()

        originalsize = os.stat(infile).st_size
        newsize = os.stat(midfile).st_size

        exe2 = subprocess.Popen(f"{huffman_impl} -d {midfile} {outfile}", shell=True)
        exe2.wait()

        originalfile = open(infile).read()
        newfile = open(outfile).read()

        self.assertEqual(originalfile, newfile)
        self.assertLess(newsize, originalsize)

    @weight(15)
    def testBinaryInput(self):
        """Test on binary input, that an image can be reconstituted"""
        # check that the image is properly compressed and reconstituted
        # note that we do not expect any actual compression in this case
        infile = 'dijkstra.png'
        midfile = 'midfile'
        outfile = 'dijkstra_out.png'
        exe = subprocess.Popen(f"{huffman_impl} -c {infile} {midfile}", shell=True)
        exe.wait()

        exe2 = subprocess.Popen(f"{huffman_impl} -d {midfile} {outfile}", shell=True)
        exe2.wait()

        originalhash = hashlib.md5(open(infile, 'rb').read()).hexdigest()
        outputhash = hashlib.md5(open(outfile, 'rb').read()).hexdigest()

        self.assertEqual(originalhash, outputhash)
