#!/usr/bin/python3
#-*- coding:utf-8 -*-

from sys import exit
#from multiprocessing import Queue,Process
############计算相似度################
#def cal1(tag,queue):
#    sums=0
#    for i in tag:
#        sums+=ord(i)
#    queue.put(sums)
#    
#def calculate(tag1,tag2):
#    que1=Queue();que2=Queue()
#    p1=Process(target=cal1,args=(tag1,que1))
#    p2=Process(target=cal1,args=(tag2,que2))
#    p1.start();p2.start();p1.join();p2.join()
#    if abs(que1.get()-que2.get())<19:
#        print(tag1,end='  ')

#########1段###########################

def is6r(): #是否编报降水组6RRR1
    return input('\n是否编报降水组6RRR1:\n1.编报\n3.无降水\n4.补充报/有降水但未观测/观测值无法确定:')

def is7w(): #是否编报现在、过去天气组
    return input('\n是否编报现在/过去天气组:\n人工组:\n\t1.编报\n\t2.无相应天气现象\n\t3.未观测\n自动化组:\n\t4.编报\n\t5.无相应天气现象\n\t6.未观测:')

def is1():  #1段编报
    flag=input('\n区站号(5位整数):')
    return flag

def yun_heigth():   #云高
    heigth=input('\n云高(整数)：')
    try:
        if heigth=='无云':
            return 9
        elif '不明' in heigth:
            return 'x'
        elif (int(heigth)-50)<0:
            return 0
        elif (int(heigth)-100)<0:
            return 1
        elif (int(heigth)-200)<0:
            return 2
        elif (int(heigth)-300)<0:
            return 3
        elif (int(heigth)-600)<0:
            return 4
        elif (int(heigth)-1000)<0:
            return 5
        elif (int(heigth)-1500)<0:
            return 6
        elif (int(heigth)-2000)<0:
            return 7
        elif (int(heigth)-2500)<0:
            return 8
        else:
            return 9
    except:
        print('错误，或许你可以写‘无云’或任何包含‘不明’的字段')
        return -1

def vision():   #能见度
    length=float(input('\n有效能见度（两位数字，如0.9，4.5）:'))
    if (length-5)<5:
        if length<0.1:
            return '00'
        elif length<1.0:
            return '0'+str(int(10*length))
        else:
            return str(int(10*length))
    elif length<30:
        return str(length+50)
    else:
        return str((length-30)//5+80)

def yun_volume():   #云量
    try:
        dic={1:1,2:2,3:2,4:3,5:4,6:5,7:6,8:6,9:7,10:8}
        res=input('\n云量:')
        if '无云' in res:
            return 0
        elif '微' in res:
            return 1
        elif '无法' in res:
            return 9
        elif '未观测' in  res:
            return 'x'
        else:
            return dic[int(res)]
    except KeyboardInterrupt:
        exit('\n已终止')
    except:
        print('无法处理输入结果，请参考下列信息：\n1.无云时请写：无云\n2.微量时输入：微量\n3.无法观测时输入：无法观测\n4.未观测时输入：未观测\n5.正常观测时输入1-10的整数')
        return -1

def wind_loca():    #风向
    loca=input('\n风向(字母)\n静风可输入0:')
    dic={'0':'00','NNE':'02','NE':'04','ENE':'07','E':'09','ESE':'11','SE':'14','SSE':'16','S':'18','SSW':'20','SW':'22','WSW':'25','W':'27','WNW':'29','NW':'32','NNW':'34','N':'36'}
    try:
        return dic[loca.upper()]
    except KeyError:
        print('输入有误，请参考以下键值:')
        for i in dic.keys():
            print(i,end='  ')
        print('')
        return -1

def wind_velo():    #风速
    velo=input('\n风速(整数)\n小数四舍五入,个位前面加0，如:09,18:')
    return velo

def temp():     #温度
    flag=input('\n1.气温 2.露点温度：')
    temp=input('\n输入温度\n以0.1度为单位，应为3位整数\n负号一起输入即可:')
    if '-' in temp:
        return flag+'1'+temp[1:]
    else:
        return flag+'0'+temp

def pres():     #气压
    flag=input('\n3.本站气压 4.海平面气压:')
    pres=input('\n气压\n以0.1hpa为单位，应为4位整数\n千位请舍去，如1024.5只填“0245”:')
    return flag+pres

def pres_chan():    #气压变化倾向，变化量
    while 1:
        which=input('\n过去三小时气压变化倾向:\n2.上升 4.不变 7.下降:')
        if which in ['2','4','7']:
            break
        else:
            print('输入有误!')
    many=input('\n气压变化量，以0.1hpa为单位\n千位舍去，应为三位整数:')
    print('结果:','5'+which+many)

def rain(flag):     #降水量
    if flag=='1':
        volume=input('\n降水量，以毫米为单位:')
        if volume<1:
            print('结果为:','6'+str(990+int(int(volume)*10))+'1')
        else:
            for i in range(len(volume)):
                volume='0'+volume
            print('结果为:','6'+volume+'1')
    else:
        pass

#def 
###########3段##############################

def is3():
    return '333XX'

def pres_temp():    #气压＋气温
    print("绝对值不到0.5时统一位'0'")
    temp=input('\n本站气温变量\n小数四舍五入，负数加50\n应为两位整数，不足补0:')
    pres=input('\n本站气压变量\n小数四舍五入，负数加50\n应为两位整数，不足补0:')
    return '0'+pres+temp


def iihvv():    #
    tag3=is6r()
    tag4=is7w()
    while 1:
        tag=yun_heigth()
        if tag!=-1:
            tag1=str(tag)
            break
    while 1:
        tag=vision()
        if tag!=-1:
            tag2=str(tag)
            break
    print('结果:',tag3+tag4+tag1+tag2)
    return tag3,tag4

def nddff():    #
    while 1:
        tag=yun_volume()
        if tag!=-1:
            tag1=str(tag)
            break
    while 1:
        tag=wind_loca()
        if tag!=-1:
            tag2=str(tag)
            break
    while 1:
        tag=wind_velo()
        if tag!=-1:
            tag3=str(tag)
            break
    print('结果:',tag1+tag2+tag3)

if __name__=='__main__':
    6r,7w=iihvv();nddff();
    while 1:
        tag=temp()
        if tag!=-1:
            print(str(tag))
            break
    while 1:
        tag=pres()
        if tag!=-1:
            print(str(tag))
            break
    pres_chan();rain(6r);
    print('\n编报结果已全部输出！')
