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
    # 'sarvar':'mi 10'}
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























