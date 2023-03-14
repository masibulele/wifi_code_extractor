#1. Import the subprocess module 
import subprocess


#2. Get the metadata of the wlan(wifi) with the help of check_output method 
meta_data= subprocess.check_output(['netsh','wlan','show','profiles'])
#3. Decode the metadata and split the meta data according to the line 
data= meta_data.decode('utf-8',errors= 'backslashreplace')

#4. From the decoded metadata get the names of the saved wlan networks 
data= data.split('\n')

profiles=[]

for line in data:
    if 'All User Profile' in line:

        line=line.split(':')
        name=line[1]
        name= name[1:-1]

        profiles.append(name)
#5. Now for each name again get the metadata of wlan according to the name 
#print(profiles)
print('{:<30}| {:<}'.format('Wi-fi name', 'password'))
print('______________________________________________')

#6. Start try and catch block and inside the try block, decode and split this metadata and get the password of the given wifi name
for n in profiles:
     try:
         
         results= subprocess.check_output(['netsh','wlan','show','profile',n,'key=clear'],shell=True)
        
         results= results.decode('utf-8',errors='backslashreplace')
         results= results.split('\n')

         results= [data.split(':')[1][1:-1] for data in results if 'Key Content' in data]

         try:
             print('{:<30}|{:<}'.format(n,results[0]))

         except IndexError:
             print('{:<30}|{:<}'.format(n," "))
     except subprocess.CalledProcessError:
        print('error in running subprocess of network')

#7. Print the password and the wifi name and print blank if there is no password 
#8. In except block if process error occurred print encoding error occurred 
