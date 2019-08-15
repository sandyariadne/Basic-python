
konco = ["Yati", "Indah", "Yanto", "Hadi", "Sulpy"]
konco[1] ="Joko"
print(konco[1])
print(konco[-1])
print(konco[1:])
print(konco[0:4])

lucky_number = [4, 8, 15, 16, 23, 42]
konco1 = ["Yati", "Indah", "Yanto", "Hadi", "Sulpy"]
konco1.extend(lucky_number)
konco1.append("Yoki")
konco1.pop()
konco1.clear()
print(konco1)

lucky_number = [4, 8, 15, 16, 23, 42]
konco2 = ["Yati", "Indah", "Yanto", "Hadi", "Sulpy"]
konco2.insert(1, "Molyono")
konco2.remove("Hadi")
print(konco2.index("Yanto"))
print(konco2)

lucky_number = [4, 8, 15, 16, 23, 42]
konco3 = ["Yati", "Indah", "Yanto", "Yanto", "Yanto", "Yanto", "Hadi", "Sulpy"]
print(konco3.count("Yanto"))
konco3.sort()
print(konco3)
lucky_number.reverse()
print(lucky_number)

konco4 = konco.copy()
print(konco4)