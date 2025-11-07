def add_time(start, duration, day=''):
    new_time = ''
    
    start_time, check_meridian = start.split()
    start_hour, start_minute = start_time.split(':')

    duration_hour, duration_minute = duration.split(':')

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    time_in_hours = int(start_hour)
    if check_meridian == 'PM':
        time_in_hours += 12
    
    time_in_minutes = time_in_hours*60 + int(start_minute)

    duration_in_minutes = int(duration_hour)*60 + int(duration_minute)

    time_in_minutes += duration_in_minutes

    meridian = 'AM'
    day_count = time_in_minutes // 1440

    time_in_minutes %= 1440

    if time_in_minutes >= 720:
        meridian = 'PM'
        time_in_minutes -= 720

    if time_in_minutes // 60 == 0:
        new_time += '12'
    else:
        new_time += str(time_in_minutes // 60)

    new_time += ':'

    if time_in_minutes % 60 < 10:
        new_time += '0' + str(time_in_minutes % 60)
    else:
        new_time += str(time_in_minutes % 60)
        
    new_time += ' ' + meridian

    if day != '':
        day_number = next((i for i, d in enumerate(days) if d.lower() == day.lower()), None)
        day_number += day_count
        day_number %= 7        
        new_time += ', ' + days[day_number]

    if day_count == 1:
        new_time += ' (next day)'
    elif day_count > 1:
        new_time += f' ({day_count} days later)'
        
    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00'))
print(add_time('8:16 PM', '466:02'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('8:16 PM', '466:02', 'tuesday'))