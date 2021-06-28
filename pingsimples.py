import os 
print("#" *68)
ip_ou_host = input("Digite o ip ou host a ser verificado: ")
print("-" *68)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" *68)