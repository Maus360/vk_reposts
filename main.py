from time import sleep
import random
import re
import vk

def main():
    session=vk.AuthSession(app_id='5587961', user_login='*****', user_password='*****',scope='wall')
    api=vk.API(session)
    find=input('Введи запрос vk, например "розыгрыш репост": ')
    period=int(input('сколько последних секунд учитывать? '))
    count=0
    while True:
        time=api.utils.getServerTime()
        print('{} ок подожди минуту'.format(time))
        a=api.newsfeed.search(q=find,start_time=time-period,end_time=time, count=20)
        for i in a[1:]:
            query = 'wall' + str(i['from_id'])  + '_' + str(i['id'])
            count += 1
            print('{0}: {1}'.format(count,i['text']))
            try:
            	api.wall.repost(object=query)

            except:
                print('репост не сделан')
            try:
            	api.likes.add(type='post', owner_id=i['from_id'], item_id=i['id'])
            except:
                print('лайк не поставился')
            sleep(random.randint(10,30))
        print('перерыв')
        sleep(100)
if __name__ == '__main__':
    main()
