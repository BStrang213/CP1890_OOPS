from datetime import datetime, time

def main():
    print("The Timer Program")

    input("Press Enter to Start...")
    start = datetime.now()
    print(f"Start Time: {start}")
    print()

    input("Press Enter to Stop...")
    stop = datetime.now()
    print(f"Stop Time: {stop}")
    print()

    elapsed = start - stop
    days = elapsed.days
    minutes = elapsed.seconds // 60
    seconds = elapsed.seconds % 60
    microseconds = elapsed.microseconds

    hours = minutes // 60
    minutes = minutes % 60

    timer = time(hours, minutes, seconds, microseconds)

    if days > 0:
        print(f"Days: {days}")
    print(f"Time: {timer}")


if __name__ == "__main__":
    main()
