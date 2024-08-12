import threading as t
from time_stuff import get_time, timestamp, kill_time
import os


def func():
    print(f"Starting: ({os.getpid()})... ({timestamp()})")
    kill_time()
    print(f"{os.getpid()} finished! ({timestamp()})")


@get_time
def main():
    thread = t.Thread(target=func)
    thread2 = t.Thread(target=func)

    thread.start()
    thread2.start()

    thread.join()
    thread2.join()


if __name__ == "__main__":
    main()
