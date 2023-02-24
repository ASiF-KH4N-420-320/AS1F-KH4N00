import os, platform

def Run():

        bit = platform.architecture()[0]

        if bit == '64bit':

            import asifxzx

        elif bit == '32bit':

            import asif

Run()
