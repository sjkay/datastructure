import os

def search():
    filenames = os.listdir('./input/')
    for filename in filenames:
        print (filename)