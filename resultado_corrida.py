import syslog
import datetime as dt

cod_drivers = {
    '038' : {
        'name' : 'F. Massa',
        'team' : 'Ferrari',
        'country' : 'Brazil'
    },
    '033' : {
        'name' : 'R. Barrichello',
        'team' : 'Williams',
        'country' : 'Brazil'
    },
    '002' : {
        'name' : 'K. Raikkonen',
        'team' : 'McLaren',
        'country' : 'Finland'
    },
    '023' : {
        'name' : 'M. Webber',
        'team' : 'Red Bull',
        'country' : 'Australia'
    },
    '015' : {
        'name' : 'F. Alonso',
        'team' : 'Ferrari',
        'country' : 'Spain'
    },
    '011' : {
        'name' : 'S. Vettel',
        'team' : 'Red Bull',
        'country' : 'Germany'
    }
}

def race_log(log):

    race = []

    for line in log.splitlines()[1:]:
        line = line.split()
        line.remove(line[2])
        race.append(line)

    return race

def cod_drivers(log):

    drivers = []

    for line in log.splitlines()[1:]:
        line = line.split()
        drivers.append(line[1])

    drivers = list(set(drivers))
    drivers.sort()

    return drivers

def race_by_driver(race,cod_drivers):

    race_driver = []

    for cod_driver in cod_drivers:
        race_driver.append([x for x in race if x[1] == cod_driver])

    return race_driver

def last_lap(race_driver):

    result_last_lap = []

    for d in race_driver:
        last_lap  = d[-1]
        result_last_lap.sort()

    return result_last_lap

def cal_race_time(race,cod_driver):

    time_list = [dt.datetime.strftime(x[-2], '%M:%S.%f')
                 for x in race if x[1] == cod_driver]
    sum_minutes = 0
    sum_seconds = 0
    sum_microseconds = 0

    for time in time_list:
        sum_minutes += time.minute
        sum_seconds += time.second
        sum_microseconds += time.microsecond

        total_time = dt.timedelta(
            minutes=sum_minutes,
            seconds=sum_seconds,
            microseconds=sum_microseconds)

        total_time_format = dt.datetime.strftime(str(total_time), '%H:%M:%S.%f')
        total_time_format = total_time_format.strftime('%H:%M:%S.%f')[-3]

        return total_time_format

def race_results():

        header = "Posição\tCódigo Piloto\tNome Piloto\t Voltas Completadas\tTempos Total"
        print(header)
        position = 1
        results = last_lap

        for r in results:
            total_time =cal_race_time(race_log, r[1])
            print("{0}\t{1:15} {2:15} {3:23} {4}".format(
                position, r[1], r[2], r[3], total_time))
            position += 1

def main ():
    with open('test_f1.log', newline='') as file:
        read_file = file.read()

        log = race_log(read_file)
        cod_driver = cod_drivers(read_file)
        race_drivers = race_by_driver(log, cod_driver)
        result_last_lap = last_lap(race_log)



    print("{} is the winner!\n".format(last_lap[0][2]))
    race_results(race_log, last_lap)


    if __name__ == "__main__":
        main()