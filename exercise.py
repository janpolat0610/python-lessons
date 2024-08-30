# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:27:44 2024

@author: User
"""
# print('Hello World')




# car_0={'cars':'ferrari','ren':'qizil'}
# print(car_0['cars'])
# print(car_0['ren'])


# en_uz={'apple':'alma','apricot':'erik'}

# miywe={'alma':10000,'garbiz':700,'juzim':20000}
# print(f"Alma bahasi {miywe['alma']} som")


# student={'ati familyasi':'Ernur','jasi':14,'t_jili':2010}
# print(f"student {student['ati familyasi']},jasi {student['jasi']} de, {student['t_jili']} -jili tuwilgan")
# student['kurs']=4
# student['fakultet']='IT'
# student['ati familyasi']='Bayram'

# print(student.items())
# for kalit,qiymat in student.items():
#     print(f"kalit:{kalit}")
#     print(f'qiymat:{qiymat}\n')
    
# telefonlar={
#     'ali':'iphone x',
#     'vali':'galaxy s10',
#     'sarvar':'mi 10'}
# for k,q in telefonlar.items():
#     print(f'{k}ning telefoni {q}')
# for k in telefonlar.keys():
#     print(k)

# for q in telefonlar.values():
#     print(q)

# ism=input('salom ismingiz nima?\n')
# savol=f'salom {ism.title()}. yoshingiz nechida? \n'
# yosh=input(savol)
# yosh=int(yosh)
# boy=input(f'{ism} boyingiz nechi metr? \n')
# boy=float(boy)
# print(f'ismi : {ism}',
#       f'yoshi : {yosh}',
#       f'boyi : {boy}')


# son=1
# while  son<=5:
#     print(son, end=" ")
#     son=son+1
# print('Tawsildi')


# print('sannin kvadratin shigariwshi programma')
# san='san kiritin'
# san += "(eger toqtatpaqshi bolsaniz 'exit' deb jazin )"
# manis=' '
# while manis != 'exit':
#     manis=input(san)
#     if manis != 'exit':
#         print(float(manis)**2)
# print('programma toqtadi')


# 5

# print('sannin kvadratin shigariwshi programma')
# san='san kiritin'
# san += "(eger toqtatpaqshi bolsaniz 'exit' deb jazin )"
# belgi=True
# while belgi:
#     manis=input(san)
#     if manis=='exit':
#         belgi=False
#     else:
#         print(float(manis)**2)
# print('programma toqtadi')
    


# print('jaqin doslar dizimin duzemiz')
# doslar=[]
# n=1
# while True:
#     soraw=f'{n}-dosiniz kim? \n'
#     ati=input(soraw)
#     doslar.append(ati)
#     qaytalaw=input('jane dos qosasizba? awa/yaq \n')
#     n+=1
#     if qaytalaw !='awa':
#         break
#     elif qaytalaw != 'awa' or 'yaq':
#         continue

# print(doslar)


 #                Funkciya

# 1

# def salember():
#     """Assalawma aleykum funksiyasi"""
#     print('assalawma aleykum!')
 
# salember()

# 2


# def salemles(ati):
#     """"Salemlesetugin funksiya"""
#     print(f'assalawma aleykum {ati.title()}')

# a=input('atiniz \n')
# salemles(a)

# print(salemles.__doc__)





# def jas_esaplawshi(ati,t_jili):
#     """Jas esaplawshi funkiya"""
#     print(f'{ati.title()} {2024-t_jili} jasda')
# at=input('atiniz \n>>>')
# tjili=int(input('tuwilgan jiliniz \n>>>'))

# jas_esaplawshi(at,tjili)


# def toliq_at_jasa(ati,familyasi):
#     """Toliq at jasawshi funkciya"""
#     toliq_ati=f'{familyasi.title()} {ati.title()}'
#     return toliq_ati

# at=input('atiniz \n>>>')
# familya=input('familyaniz \n>>>')
# oquwshi=toliq_at_jasa(at, familya)
# print(oquwshi)






# def toliq_at(ati,familyasi,akesinin_ati=""):
#     if akesinin_ati:
#         toliq_ati=f'{ati} {akesinin_ati} {familyasi}'
#     else:
#         toliq_ati=f'{ati} {familyasi}'
#     return toliq_ati.title()

# oqiwshi=input('atiniz?\n>>>')
# familya=input('familyaniz\n>>>')
# atasinin_ati=input('akenizdin ati?(qalewiniz)\n>>>')
# toliq_at=toliq_at(oqiwshi,familya,atasinin_ati)
# print(f'assalawma aleykum {toliq_at}')     


# def bahalaw(atlari):
#     '''bahalaw ushin funkciya'''
#     bahalar={}
#     while atlari:
#         at=atlari.pop()
#         baha=input(f'{at.title()} ga baha qoyin\n>>>')
#         bahalar[at]=int(baha)
#     return bahalar


# oquwshilar={'Janpolat','Ernur','Alisher'}
# bahalar=bahalaw(oquwshilar[:])
# print(bahalar)



# def bazar(kompanya,model,jili,reni,probeg,bahasi=None):
#     """avto bazar"""
#     avto={'kompanya':kompanya,
#               'model':model,
#               'jili':jili,
#               'reni':reni,
#               'probeg':probeg,
#               'bahasi':bahasi}
#     return avto

# k=input('kompanya \n>>>')
# m=input('model \n>>>')
# j=int(input('jili \n>>>'))
# r=input('reni\n>>>')
# p=int(input('probeg \n>>>'))
# b=int(input('bahasi (jaziw iqtiyariy) \n>>>'))
# mashina=bazar(k,m,j,r,p,b)
# print(mashina)


#                  math
# import math
# a='sannin korenin tabiwshi programma'
# print(a)
# b='qalegen san kiritin(eger toqtatpaqshi bolsaniz exit dep jazin)   '
# manis=""
# while manis!='exit':
#     manis=input(b)
#     if manis!='exit':
#         manis=int(manis)
#         print(math.sqrt(manis))
# print('programma toqtadi')
        
    
    
# import math
# a='sannin korenin tabiwshi programma'
# print(a)
# b='qalegen san kiritin(eger toqtatpaqshi bolsaniz exit dep jazin)   '
# manis=""
# qa='dareje kiritin   '
# dareje=''
# while manis!='exit':
#     manis=input(b)
#     if manis!='exit':
#         manis=int(manis)
#         dareje=int(input(qa))
#         print(math.pow(manis,dareje))
#     else:
#         break
# print('programma toqtadi')
    

# import math

# x=100

# print(math.sqrt(x))

# print(math.pow(5,2))

# print(math.pi)   
    

#                     random


# import random as r 

  # randint
# a=r.randint(1, 10)
# print(a)

# sanlar=list(r.sample(range(100),10))
# print(sanlar)


# choise 

# atlar=['jasur','bayram','ernur','alisher','musa']
# b=r.choice(atlar)
# print(b)     
# print(r.choice(b))
    
#   shuffle


# a=list(range(1,25))
# print(a)
# r.shuffle(a)
# print(a)



#         lambda

# import math


# uzinliq= lambda pi , r : 2*pi*r
# print(uzinliq(math.pi,10))

# def dareje(n):
#     return lambda x : x**n

# kvadrat=dareje(2)
# kub=dareje(3)

# a=int(input())
# b=kub(a)
# print(b)



# from math import sqrt


# def juppa(x):
#     '''sannin jup ya taqligin aniqlawshi programma'''
#     return x%2==0


# print('sannin jup ya taqligin aniqlaymiz')
# a=int(input('qalegen san kiritin \n>>>'))
# print(juppa(a))



# jupsanlar=list(filter(juppa,sanlar))


# jupsanlar=list(filter(lambda x : x%2==0,sanlar))

# print(jupsanlar)


# miyweler=['banan','erik','alma','almurt','anar','anjir','qareli']

# harip='a'

# b=list(filter(lambda miywe : miywe.startswith(harip),miyweler))

# print(b)


# import random as r

# def son_top(x=10):
#     '''san tabiw'''
#     print('san tabiw oyini, men bir san oyladim taba alasizba?')
#     c=r.randint(1,x)
#     san=('sandi tabiwga hareket etin' )
#     a=True
#     urinis=0
#     while a:
#         urinis=urinis+1
#         san=int(input())
#         if san<c:  
#             print(f'men oylagan san {san} dan ulken')          
#         elif san>c:
#             print(f'men oylagan san {san} dan kishi')
#         else:
#             break
#     print('                                       ')
#     print(f'qutliqlayman men oylagan san {c} edi siz oni {urinis} urinisda taptiniz')
#     return urinis


# def san_tap_pc(x=10):
#     print('men siz oylagan sandi tabaman')
#     joqari=x
#     tomen=1
#     urinis=0
#     while True:
#         urinis=urinis+1
#         if tomen!=joqari:
#             san=r.randint(tomen,joqari)
#         else:
#             san=tomen
#         a=input(f'siz {san} sanin oyladiniz duris bolsa d eger siz oylagan san {san} saninan ulken bolsa + kishi bolsa - di jiberin  >>>')
#         if a=='-':
#             joqari=san-1 
#         elif a=='+':
#             tomen=san+1
#         elif a=='d':
#             break
#     print('                                       ')
#     print(f'men siz oylagan sandi {urinis} urinista taptim')
#     return urinis
    
    
# def play(x=10):
#     'oyin baslaw'
#     print('oyin baslandi')
#     jane=True
#     while jane:
#         urinislar_user=son_top(x)
#         urinislar_pc=san_tap_pc(x)
#         if urinislar_user<urinislar_pc:
#             print('                                       ')
#             print('BUL OYINDA SIZ UTTINIZ')
#             print('                                       ')
#         elif urinislar_user>urinislar_pc:
#             print('                                       ')
#             print('BUL OYINDA MEN UTTIM')
#             print('                                       ')
#         else:
#             print('                                       ')
#             print('DOSLIQ JENDI')
#             print('                                       ')
#         jane=int(input('Jane oynawdi qaleysizba? awa(1)/yaq(0) \n>>>'))
        
# print(play())




class Oqiwshi:
    def __init__(self,ati,familya,tjil):
        self.ati=ati
        self.familya=familya
        self.tjil=tjil
    def tanistir(self):
        return (f'oqiwshi {self.ati} {self.familya}, {self.tjil}-jili tuwilgan')

ati=input()
familya=input()
tjil=int(input())
        
oqiwshi = Oqiwshi(ati,familya,tjil)



