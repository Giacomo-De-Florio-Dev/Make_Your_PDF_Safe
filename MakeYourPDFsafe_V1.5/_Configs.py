import json

while True:
    try:
        with open("Configs.json", "r") as Config_File:
            Get_Configs = json.load(Config_File)

        Check_Platform = Get_Configs["Platform_Check_System"]["Enable_The_Platform_Check"]
        Supported_Os = Get_Configs["Platform_Check_System"]["Which_Platforms_Can_Execute_This_Program"]

        # if no errors occur...

        break

    except:

        with open("Default_Configs.json") as Config_File:
            Get_Configs = json.load(Config_File)

        with open("Configs.json", "w") as Config_File:
            Set_Configs = json.dump(Get_Configs, Config_File, indent=4, sort_keys=False)

            # repeat the cycle to get the values...

            continue
