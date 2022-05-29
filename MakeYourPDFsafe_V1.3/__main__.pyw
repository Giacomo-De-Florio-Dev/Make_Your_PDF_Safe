import check_plat
import mainpage

if check_plat.platCheck() == "PLAT:OK":
    mainpage.mainpage()

elif check_plat.platCheck() == "PLAT:ERROR":
    exit()