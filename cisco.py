from netmiko import ConnectHandler
from datetime import datetime
import csv, os.path

'''
    The following block of code handles timestamp functions
'''
# Time stamps to log how long this particular script takes to run through the all_juniper device list.
entire_time_begin = datetime.now()


with open('device_info.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    username = raw_input('Please enter your username: \n')
    password = raw_input('Please enter your password: \n')
    for row in reader:
        start_time = datetime.now()  # grab a timestamps for additional information
        #print(row['hostname'], row['description'])
        hostname = row['hostname']
        #username = row['username']
        #password = row['password']
        switch = {'device_type': 'cisco_ios', 'ip': hostname, 'username': username, 'password': password, 'verbose': False, }
        print switch
        ssh_session = ConnectHandler(**switch)
        hostname = ssh_session.find_prompt() # a netmiko function that retrieves current line from terminal
        hostname = hostname.replace("#", "") # strips out the # sign from the Cisco prompt
        print("=" * 64 + "\n" + 29 * " " + "% s \n" + "=" * 64) % hostname
        # output = ssh_session.send_command('show power inline | exclude Interface|Watt|----')
        output = "Available:847.0(w)  Used:19.4(w)  Remaining:827.6(w)\n\nGi0/1     auto   off        0.0     n/a                 n/a   60.0\nGi0/2     auto   off        0.0     n/a                 n/a   60.0\nGi0/3     auto   off        0.0     n/a                 n/a   60.0\nGi0/4     auto   off        0.0     n/a                 n/a   60.0\nGi0/5     auto   off        0.0     n/a                 n/a   60.0\nGi0/6     auto   off        0.0     n/a                 n/a   60.0\nGi0/7     auto   off        0.0     n/a                 n/a   60.0\nGi0/8     auto   off        0.0     n/a                 n/a   60.0\nGi0/9     auto   off        0.0     n/a                 n/a   60.0\nGi0/10    auto   off        0.0     n/a                 n/a   60.0\nGi0/11    auto   off        0.0     n/a                 n/a   60.0\nGi0/12    auto   off        0.0     n/a                 n/a   60.0\nGi0/13    auto   off        0.0     n/a                 n/a   60.0\nGi0/14    auto   off        0.0     n/a                 n/a   60.0\nGi0/15    auto   off        0.0     n/a                 n/a   60.0\nGi0/16    auto   off        0.0     n/a                 n/a   60.0\nGi0/17    auto   off        0.0     n/a                 n/a   60.0\nGi0/18    auto   off        0.0     n/a                 n/a   60.0\nGi0/19    auto   off        0.0     n/a                 n/a   60.0\nGi0/20    auto   off        0.0     n/a                 n/a   60.0\nGi0/21    auto   off        0.0     n/a                 n/a   60.0\nGi0/22    auto   off        0.0     n/a                 n/a   60.0\nGi0/23    auto   off        0.0     n/a                 n/a   60.0\nGi0/24    auto   off        0.0     n/a                 n/a   60.0\nGi0/25    auto   off        0.0     n/a                 n/a   60.0\nGi0/26    auto   off        0.0     n/a                 n/a   60.0\nGi0/27    auto   off        0.0     n/a                 n/a   60.0\nGi0/28    auto   off        0.0     n/a                 n/a   60.0\nGi0/29    auto   off        0.0     n/a                 n/a   60.0\nGi0/30    auto   on         4.0     Ieee PD             1     60.0\nGi0/31    auto   off        0.0     n/a                 n/a   60.0\nGi0/32    auto   off        0.0     n/a                 n/a   60.0\nGi0/33    auto   off        0.0     n/a                 n/a   60.0\nGi0/34    auto   off        0.0     n/a                 n/a   60.0\nGi0/35    auto   off        0.0     n/a                 n/a   60.0\nGi0/36    auto   off        0.0     n/a                 n/a   60.0\nGi0/37    auto   off        0.0     n/a                 n/a   60.0\nGi0/38    auto   off        0.0     n/a                 n/a   60.0\nGi0/39    auto   off        0.0     n/a                 n/a   60.0\nGi0/40    auto   off        0.0     n/a                 n/a   60.0\nGi0/41    auto   off        0.0     n/a                 n/a   60.0\nGi0/42    auto   off        0.0     n/a                 n/a   60.0\nGi0/43    auto   off        0.0     n/a                 n/a   60.0\nGi0/44    auto   off        0.0     n/a                 n/a   60.0\nGi0/45    auto   off        0.0     n/a                 n/a   60.0\nGi0/46    auto   off        0.0     n/a                 n/a   60.0\nGi0/47    auto   off        0.0     n/a                 n/a   60.0\nGi0/48    auto   on         15.4    AIR-CAP3502I-A-K9   3     60.0\n"
        '''
            The following block of code handles CSV functions.
        '''
        # Define the .csv file path and name. This is currently set up for an OS X environment
        userhome = os.path.expanduser('~')
        csvfile = os.path.join(userhome, 'Dropbox', hostname + '.csv')
        myfile = open(csvfile, 'wb')
        # Here we will create the CSV column names to store data into
        fieldnames = ['interface', 'admin', 'oper', 'power', 'device', 'class_var', 'max']
        # Now we create a variable called 'writer' and concatenate the csv file path and fieldnames
        writer = csv.DictWriter(myfile, fieldnames=fieldnames)
        # Finally we write the header information to the CSV file
        writer.writeheader()
        '''
            Try Loop
        '''
        try:
            splitlines = output.splitlines()
            first_line = splitlines[0]
            split = first_line.split()
            power_used = split[1]
            print "Total Power " + power_used + "\n"
            output = splitlines[2:]
            print "The following interfaces are using PoE:"
            '''
                For Loop
            '''
            for each_line in output:
                line = each_line.split()
                interface = line[0]
                admin = line[1]
                oper = line[2]
                power = line[3]
                power_int = int(float(power))
                device = line[4]
                class_var = line[5]
                max = line[6]
                # We now create a dictionary based on the newly created variables.
                row = {'interface': interface, 'admin': admin, 'oper': oper,
                       'power': power, 'device': device, 'class_var': class_var, 'max': max}
                # Now we take the dictionary row and right it as a row to the CSV file
                writer.writerow(row)
                # haven't googled why we need to clear the row, but that's apparently what we do.
                row.clear()
                if power_int > 0:
                    print ""
                    print "Interface :" + interface
                    print "Device :" + device
                    print "Class :" + class_var
                    print "Power :" + power
        except IndexError:
            print "PoE isn't supported on this device"
            continue
        end_time = datetime.now()
        total_time = end_time - start_time
        print("\ntotal time spent on " + hostname + ": " + str(total_time) + '\n')

    final_time = datetime.now()
    complete_time = final_time - entire_time_begin
    print("\n\nFinished running the script in " + str(complete_time) + " seconds")
