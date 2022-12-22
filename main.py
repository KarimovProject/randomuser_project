from random_user import RandomUser
import pprint

# Create a new instance of the RandomUser class
user = RandomUser()
get_user_full_about ={
    'first_name':user.get_first_name(),
    'last_name':user.get_last_name(),
    'phone': user.get_phone(),
    'picture':user.get_picture(),
    'email':user.get_email(),
    'location':user.get_location()
}
get_users_num = 20
s= 0
get_about_user=[]
while s!=get_users_num:
    
    get_about_user.append(get_user_full_about)
    s+=1
    
pprint.pprint(get_about_user)