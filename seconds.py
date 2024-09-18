from datetime import datetime


def solution_2(time):
    time_object = datetime.strptime(time, "%H:%M:%S").time()
    return time_object.hour*3600 + time_object.minute*60 + time_object.second


if __name__ == '__main__':
    print(solution_2("12:34:56"))