from netmiko import ConnectHandler
from device_credientials import all_devices
from datetime import datetime

__author__ = 'Calvin Remsburg'
# (c) 2016, packetferret.

begin_time = datetime.now()
output = "Available:847.0(w)  Used:19.4(w)  Remaining:827.6(w)\nGi0/1     auto   off        0.0     n/a                 n/a   60.0\nGi0/2     auto   off        0.0     n/a                 n/a   60.0\nGi0/3     auto   off        0.0     n/a                 n/a   60.0\nGi0/4     auto   off        0.0     n/a                 n/a   60.0\nGi0/5     auto   off        0.0     n/a                 n/a   60.0\nGi0/6     auto   off        0.0     n/a                 n/a   60.0\nGi0/7     auto   off        0.0     n/a                 n/a   60.0\nGi0/8     auto   off        0.0     n/a                 n/a   60.0\nGi0/9     auto   off        0.0     n/a                 n/a   60.0\nGi0/10    auto   off        0.0     n/a                 n/a   60.0\nGi0/11    auto   off        0.0     n/a                 n/a   60.0\nGi0/12    auto   off        0.0     n/a                 n/a   60.0\nGi0/13    auto   off        0.0     n/a                 n/a   60.0\nGi0/14    auto   off        0.0     n/a                 n/a   60.0\nGi0/15    auto   off        0.0     n/a                 n/a   60.0\nGi0/16    auto   off        0.0     n/a                 n/a   60.0\nGi0/17    auto   off        0.0     n/a                 n/a   60.0\nGi0/18    auto   off        0.0     n/a                 n/a   60.0\nGi0/19    auto   off        0.0     n/a                 n/a   60.0\nGi0/20    auto   off        0.0     n/a                 n/a   60.0\nGi0/21    auto   off        0.0     n/a                 n/a   60.0\nGi0/22    auto   off        0.0     n/a                 n/a   60.0\nGi0/23    auto   off        0.0     n/a                 n/a   60.0\nGi0/24    auto   off        0.0     n/a                 n/a   60.0\nGi0/25    auto   off        0.0     n/a                 n/a   60.0\nGi0/26    auto   off        0.0     n/a                 n/a   60.0\nGi0/27    auto   off        0.0     n/a                 n/a   60.0\nGi0/28    auto   off        0.0     n/a                 n/a   60.0\nGi0/29    auto   off        0.0     n/a                 n/a   60.0\nGi0/30    auto   on         4.0     Ieee PD             1     60.0\nGi0/31    auto   off        0.0     n/a                 n/a   60.0\nGi0/32    auto   off        0.0     n/a                 n/a   60.0\nGi0/33    auto   off        0.0     n/a                 n/a   60.0\nGi0/34    auto   off        0.0     n/a                 n/a   60.0\nGi0/35    auto   off        0.0     n/a                 n/a   60.0\nGi0/36    auto   off        0.0     n/a                 n/a   60.0\nGi0/37    auto   off        0.0     n/a                 n/a   60.0\nGi0/38    auto   off        0.0     n/a                 n/a   60.0\nGi0/39    auto   off        0.0     n/a                 n/a   60.0\nGi0/40    auto   off        0.0     n/a                 n/a   60.0\nGi0/41    auto   off        0.0     n/a                 n/a   60.0\nGi0/42    auto   off        0.0     n/a                 n/a   60.0\nGi0/43    auto   off        0.0     n/a                 n/a   60.0\nGi0/44    auto   off        0.0     n/a                 n/a   60.0\nGi0/45    auto   off        0.0     n/a                 n/a   60.0\nGi0/46    auto   off        0.0     n/a                 n/a   60.0\nGi0/47    auto   off        0.0     n/a                 n/a   60.0\nGi0/48    auto   on         15.4    AIR-CAP3502I-A-K9   3     60.0\n"
print output


def main():
    for a_device in all_devices:
        start_time = datetime.now()  # grab a timestamps for additional information
        ssh_session = ConnectHandler(**a_device)  # creating a variable to manage the ssh connection
        hostname = ssh_session.find_prompt() # a netmiko function that retrieves current line from terminal
        hostname = hostname.replace("#", "") # strips out the # sign from the Cisco prompt
        print("=" * 64 + "\n" + 29 * " " + "% s \n" + "=" * 64) % hostname
        output = ssh_session.send_command('show power inline | exclude Interface|Watt|----')
        splitlines = output.splitlines()
        first_line = splitlines[0]
        split = first_line.split()
        power_used = split[1]
        print "Total Power " + power_used + "\n"
        output = splitlines[2:]
        print "The following interfaces are using PoE:"
        for each_line in output:
            line = each_line.split()
            interface = line[0]
            # admin = line[1]
            # oper = line[2]
            power = line[3]
            power_int = int(float(power))
            device = line[4]
            class_var = line[5]
            # max = line[6]
            if power_int > 0:
                print "Interface :" + interface
                print "Device :" + device
                print "Class :" + class_var
                print "Power :" + power
        end_time = datetime.now()
        total_time = end_time - start_time
        print("\ntotal time spent on " + hostname + ": " + str(total_time) + '\n')

if __name__ == "__main__":
    main()
final_time = datetime.now()
complete_time = final_time - begin_time
print("\n\nFinished running the script in " + str(complete_time) + " seconds")
