search_srting = "ap=14."
with open("C:\\Users\\rink\\Downloads\\Логи\\logs\\syncdb-2023-10-24.log") as file:
    while True:
        srting = file.readline()
        if srting == "":
            break
        if search_srting in srting:
            print(srting)
        #     first_id = srting.rindex("EMPS: initial=")+len(search_srting)
        #     count = ''.join(filter(str.isdigit, srting[first_id:first_id+5]))
        #     if int(count) > 59530:
        #         print(count)

# добавил коммент