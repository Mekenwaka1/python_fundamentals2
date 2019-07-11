def read_running_distance(number): 
    print("How far did person {} run (in metres)?".format(number))
    return float(input())

def read_running_time(person_number, distance):
    print("How long (in minutes) did person {} run take to run {} metres?".format(person_number, distance))
    return float(input())


def main(): 

    distance1 = read_running_distance(1)
    mins1 = read_running_time(1, distance1)
    secs1 = mins1 * 60
    speed1 = distance1/secs1

    distance2 = read_running_distance(2)
    mins2 = read_running_time(2, distance2)
    secs2 = mins2 * 60
    speed2 = distance2/secs2


    distance3 = read_running_distance(3)
    mins3 = read_running_time(3, distance3)
    secs3 = mins3 * 60
    speed3 = distance3/secs3

    secs2 = mins2 * 60
    speed2 = distance2/secs2
    secs3 = mins3 * 60
    speed3 = distance3/secs3

    if speed3 > speed2 and speed3 > speed1:
        print("Person 3 was the fastest at {} m/s".format(speed3))
    elif speed2 > speed3 and speed2 > speed1:
        print("Person 2 was the fastest at {} m/s".format(speed2))
    elif speed1 > speed3 and speed1 > speed2:
        print("Person 1 was the fastest at {} m/s".format(speed1))
    elif speed1 == speed2 and speed2 == speed3:
        print("Everyone tied at {} m/s".format(speed1))
    else:
        print("Well done everyone!")



main()