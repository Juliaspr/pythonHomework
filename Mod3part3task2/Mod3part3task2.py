s = '''Было просто пасмурно, дуло с севера,
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого,
То ли весь мир сошёл с ума, то ли я — того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
И серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''
i= int(0)

def len_five(s):
    s = s.translate(str.maketrans({'.': '', ',': '', '-': '', '!': '', '—': ''}))
    s = s.split()
    for i in range(0, len(s)):
         if len(s[i])<5:
            print (s[i])

len_five(s)
