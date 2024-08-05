#!/usr/bin/python
import unittest
import hashlib
import os
import sys
import subprocess
import array
import time
from gradescope_utils.autograder_utils.decorators import leaderboard, visibility
import util

huffman_impl = util.getProgram()

class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        pass

    @visibility('visible')
    @leaderboard("Small", "asc")
    def test_leaderboard_small(self, set_leaderboard_value=None):
        """Sets a leaderboard value for Small"""
        infile = 'bench.tiff'
        midfile = 'midfile'
        outfile = 'bench_out.tiff'
        exe = subprocess.Popen(f"{huffman_impl} -c {infile} {midfile}", shell=True)
        start = time.time()
        exe.wait()

        originalsize = os.stat(infile).st_size
        newsize = os.stat(midfile).st_size

        exe2 = subprocess.Popen(f"{huffman_impl} -d {midfile} {outfile}", shell=True)
        exe2.wait()
        end = time.time()


        originalhash = hashlib.md5(open(infile, 'rb').read()).hexdigest()
        outputhash = hashlib.md5(open(outfile, 'rb').read()).hexdigest()


        if originalsize > newsize and originalhash == outputhash:
            set_leaderboard_value(round(end - start, 3))

    @visibility('visible')
    @leaderboard("Medium", "asc")
    def test_leaderboard_medium(self, set_leaderboard_value=None):
        """Sets a leaderboard value for Medium"""
        infile = 'bench.ppm'
        midfile = 'midfile'
        outfile = 'bench_out.ppm'
        exe = subprocess.Popen(f"{huffman_impl} -c {infile} {midfile}", shell=True)
        start = time.time()
        exe.wait()

        originalsize = os.stat(infile).st_size
        newsize = os.stat(midfile).st_size

        exe2 = subprocess.Popen(f"{huffman_impl} -d {midfile} {outfile}", shell=True)
        exe2.wait()
        end = time.time()


        originalhash = hashlib.md5(open(infile, 'rb').read()).hexdigest()
        outputhash = hashlib.md5(open(outfile, 'rb').read()).hexdigest()


        if originalsize > newsize and originalhash == outputhash:
            set_leaderboard_value(round(end - start, 3))

    @visibility('visible')
    @leaderboard("Large", "asc")
    def test_leaderboard_large(self, set_leaderboard_value=None):
        """Sets a leaderboard value for Large"""
        infile = 'bench.fasta'
        midfile = 'midfile'
        outfile = 'bench_out.fasta'
        exe = subprocess.Popen(f"{huffman_impl} -c {infile} {midfile}", shell=True)
        start = time.time()
        exe.wait()

        originalsize = os.stat(infile).st_size
        newsize = os.stat(midfile).st_size

        exe2 = subprocess.Popen(f"{huffman_impl} -d {midfile} {outfile}", shell=True)
        exe2.wait()
        end = time.time()


        originalhash = hashlib.md5(open(infile, 'rb').read()).hexdigest()
        outputhash = hashlib.md5(open(outfile, 'rb').read()).hexdigest()


        if originalsize > newsize and originalhash == outputhash:
            set_leaderboard_value(round(end - start, 3))