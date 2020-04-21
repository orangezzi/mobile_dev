import matplotlib.pyplot as pyplot
#import pylab

def to_daystamp(time):
    hours, minutes, seconds_and_millisecs = time.split(":") 
    seconds, millisecs  = seconds_and_millisecs.split(".")
    hours, minutes, seconds, millisecs = int(hours), int(minutes), int(seconds), int(millisecs)
    return hours * 60 * 60 * 1_000 + minutes * 60 * 1_000 + seconds * 1_000 + millisecs


file = open("nfcapd.202002251200.txt", "r")
all_bytes_out = 0

time_and_bytes = []

for line in file.readlines():
    data = line.strip().split()
    
    time = to_daystamp(data[1])
    source = data[5].split(":")[0]
    dest = data[7].split(":")[0]
    
    bytes_out = data[11]
    bytes_count = float(bytes_out)

    if "." in bytes_out:
        byte_type = data[12]
        if byte_type == "M":
            bytes_count = bytes_count * 1024 * 1024
    
    if source == "192.168.250.59":
        all_bytes_out += bytes_count
    
    time_and_bytes.append((time, bytes_count))




kilo_bytes_all = all_bytes_out / 1024
kilo_bytes_more = kilo_bytes_all - 500
cost = 0.5 * min(kilo_bytes_all, 500)

if kilo_bytes_more > 0:
    cost += 1 * kilo_bytes_more

cost = round(cost, 2)
print("Internet cost:", cost)

time_and_bytes.sort(key=lambda x: x[0])

pyplot.xlabel('Time in mc at day start')
pyplot.ylabel('Bytes count')

x = [x[0] for x in time_and_bytes]
y = [x[1] for x in time_and_bytes]

pyplot.plot(x,y)
pyplot.savefig("chart.png")
