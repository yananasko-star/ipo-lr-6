seaarch=input("введите строку для поиска").lower()#запрашиваем  строку для поиска
with open('text.txt','r',encoding='utf-8') as f: # читаем файл
    lines=[line.strip()for line in f]
    found=[line fot line in lines if search in line.lower()] #ищем строку с подстрокой
    found.sort(key=len) #сортируем по длине
    print(f"найдено строк: {len(found)}") # выводим результаты
    for line in found:
        print(line)
