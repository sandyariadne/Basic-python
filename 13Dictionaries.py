
monthConversion = {
    1: "January",
    2: "February",
    3: "March",
    "Apr": "April",
    "Mey": "Mey",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversion[1])
print(monthConversion["Aug"])
print(monthConversion.get("Dec"))
print(monthConversion.get("Luv", "Not valid key"))
print(monthConversion)