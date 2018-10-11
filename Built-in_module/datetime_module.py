from datetime import datetime, timezone, timedelta
import re
'''
now = datetime.now()
print(now) #打印现在时间
print(now.timestamp()) #转化为1970年开始的秒数
t = now.timestamp()
print(datetime.fromtimestamp(t))#秒数转化为标准时间
print(now.strftime('%a, %b %d %H:%M'))#将现在时间字符化

'''

def to_timestamp(dt_str, tz_str):
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')#将str转化为datetime
    if re.match('^(utc|UTC)\+([0-9]|1[0-2])\:00$', tz_str):
        x = re.match('^(utc|UTC)(\+)([0-9]|1[0-2])\:00$', tz_str)
        hours_diff = int(x.group(3))
        tz_utc = timezone(timedelta(hours = hours_diff))
        dt = date.replace(tzinfo = tz_utz) #设置检测到的时区
        print(dt.timestamp())#输出utc秒数
    else:
        print('Invalid timezone input')
    
if __name__ == '__main__':
    to_timestamp('2015-1-21 9:01:30', 'UTC+5:00')