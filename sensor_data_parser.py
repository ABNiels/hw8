import sys, os

def main():
    f = open('raw_data.csv', 'r')
    data = f.read().split('\n')[2:-1]
    f.close()
    maximum = [0, 0, 0, 0, 0]
    minimum = [0, 0, 0, 0, 0]
    average = [0, 0, 0, 0, 0]
    count = 0;
    for line in data:
        count += 1
        line = [eval(temp) for temp in line.split(',')]
        for i in range(0, len(line)):
               maximum[i] = line[i] if line[i] > maximum[i] else maximum[i]
               minimum[i] = line[i] if line[i] < maximum[i] else minimum[i]
               average[i] += line[i]
    average = [num/count for num in average]
    f = open('report.txt', 'w')
    f.write('''
                     Summary of Raw Data from Sensors
           Average           Minimum Reading            Maximum Reading
Sensor 1:  {:.2f}              {}                          {}
Sensor 2:  {:.2f}              {}                          {}
Sensor 3:  {:.2f}              {}                          {}
Sensor 4:  {:.2f}              {}                          {}
Sensor 5:  {:.2f}              {}                          {}
'''.format(average[0], minimum[0], maximum[0], 
           average[1], minimum[1], maximum[1], 
           average[2], minimum[2], maximum[2], 
           average[3], minimum[3], maximum[3], 
           average[4], minimum[4], maximum[4]))

        
if __name__ == '__main__':
    main()
