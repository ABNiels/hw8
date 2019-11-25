import os
import sys
import time

def main():
    for _ in range(0, eval(sys.argv[1])):
        os.system('./tmp36raw')
        time.sleep(1)

if __name__ == '__main__':
    main()
