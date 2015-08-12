from facepy import GraphAPI
import datetime

oauth_token = 'your_token'
graph = GraphAPI(oauth_token)
friend_list = graph.get("me/friends?fields=birthday,name")

now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

for friend in friend_list['data']:
    if friend.has_key('birthday'):
        bday_array = friend['birthday'].split('/')
        if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
            bday_wish  = 'Happy Birthday'
            graph.post(friend['id']+ '/feed', 0, message = bday_wish)
            print "Wished " + friend['name']
