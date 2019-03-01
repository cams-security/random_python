import pandas as pd, re, ipaddress, sys
#creating data frames from excel/csvs
#looping through dataframe, adding IPs to array, if there is a range, expand the rangee and get each unique IP.
#Convert array into set, use set theory to determine which values are the same/missing/etc
# https://docs.python.org/2/library/stdtypes.html#set
df_1 = pd.DataFrame(pd.read_excel('')) #or pd.read_csv(PATH) if comparing csv files
df_2 = pd.DataFrame(pd.read_excel(''))
df_1_array = []
df_2_array=[]

def ip_range():
    for index, row in df_1.iterrows():
        ip = str(row['{COLUMN NAME']) #enter column name 
        if '-' in ip: #ex: 10.10.10.10 - 10.10.10.50, 10.10.10.60-10.10.10.70
            print("Range detected..expanding")
            comma_delimed = str(q_ip.split(','))
            for x in comma_delimed:
                dash_delimed = comma_delimed.split('-')
                try:
                    a = (re.findall(r'[0-9]+(?:\.[0-9]+){3}',dash_delimed[0])) #because problems with the nested list
                    b = (re.findall(r'[0-9]+(?:\.[0-9]+){3}',dash_delimed[1]))
                    start_ip = ipaddress.IPv4Address(a[0])
                    end_ip = ipaddress.IPv4Address(b[0])
                    for ip_int in range(int(start_ip), int(end_ip)):
                        df_2_array.append((ipaddress.IPv4Address(ip_int)))
                        df_2_array.append((ipaddress.IPv4Address(end_ip))) #If you want to include the last IP in the range.
                except IndexError: #occured when there was a typo in the IPs, handles index error and grabs any IPs in the string.
                    print('Index error...')
                    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip)
                    for ip in ip:
                        df_1_array.append(str(ip))
        else: #looking for individual IPs, or multiple IPs seperated by commas
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', q_ip)
            for ip in ip:
                df_1_array.append(str(ip))
    for index, row in df_2.iterrows():
        ip = str(row['{COLUMN NAME']) # enter column name
        if '-' in ip: #ex: 10.10.10.10 - 10.10.10.50, 10.10.10.60-10.10.10.70
            print("Range detected..expanding")
            comma_delimed = str(ipp.split(','))
            for x in comma_delimed:
                dash_delimed = comma_delimed.split('-')
                try:
                    a = (re.findall(r'[0-9]+(?:\.[0-9]+){3}',dash_delimed[0]))
                    b = (re.findall(r'[0-9]+(?:\.[0-9]+){3}',dash_delimed[1]))
                    start_ip = ipaddress.IPv4Address(a[0])
                    end_ip = ipaddress.IPv4Address(b[0])
                    for ip_int in range(int(start_ip), int(end_ip)):
                        df_2_array.append((ipaddress.IPv4Address(ip_int)))
                        df_2_array.append((ipaddress.IPv4Address(end_ip))) #If you want to include the last IP in the range.
                except IndexError: #occured when there was a typo in the IPs, handles index error and grabs any IPs in the string.
                    print('Index error...')
                    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip)
                    for ip in ip:
                        df_2_array.append(str(ip))
        else: #looking for individual IPs, or multiple IPs seperated by commas
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip)
            for ip in ip:
                df_2_array.append(str(ip))
def set_theory():
    print("There are " + str(len(df_1_array)) + " IPs in df_1_array")
    print(" \n" + "There are " + str(len(df_1_array)) + " IPs in df_2_array")
    print(" Performing SET operation on two lists. Which will return the amount of interesected elements...")
    set_of_df_1 = set(df_1_array)
    set_of_df_2 = set(df_2_array)
    print(" Number of common elements " + str(len(set_of_df_1 & set_of_df_2)))
    #writer1 = open('{FILE NAME}', 'a')
    #riter2 = open('{FILE NAME}' , 'a')
    for x in set_of_df_1 - set_of_df_2:
        print(str(x))
        #writer2.write(str(x) + '\n')
    for x in set_of_df_2 - set_of_df_1:
        print(str(x))
        #writer1.write(str(x) + '\n')


