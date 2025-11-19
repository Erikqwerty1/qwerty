def format_record(poveselee):
    sper = ""
    if type(poveselee) != tuple:
        raise TypeError
    if (
        type(poveselee[0]) == str
        and type(poveselee[1]) == str
        and type(poveselee[2]) == float
        and len(poveselee[0].split()) >= 2
    ):
        if len(poveselee[0].split()) == 2:
            fio = poveselee[0].split()
            fio_new = f"{fio[0].capitalize()} {fio[1][0].capitalize()}."
        if len(poveselee[0].split()) == 3:
            fio = poveselee[0].split()
            fio_new = f"{fio[0].capitalize()} {fio[1][0].capitalize()}.{fio[2][0].capitalize()}."
        sper = f"{fio_new}, гр. {poveselee[1]}, GPA {poveselee[2]:.2f}"
    else:
        raise TypeError
    return sper


poveselee = ("Иванов Иван Иванович", "BIVT-25", 4.6)
print(format_record(poveselee))
poveselee = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(poveselee))
poveselee = ("Петров Пётр", "IKBO-12", 5.0)
print(format_record(poveselee))
poveselee = ("", "IKBO-12", 5.0)
print(format_record(poveselee))
