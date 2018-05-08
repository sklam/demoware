import time
from utiliviz import record, CpuMon

def main():
    with record([CpuMon]) as r:
        print("HAHAHA")
        time.sleep(0.5)
    print(r.get_data())

if __name__ == '__main__':
    main()