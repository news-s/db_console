class Printer(object):
    def __init__(self, colors: bool):
        self.colors_imported = colors
        if self.colors_imported == True:
            import colorama
            self.colorama = colorama
        else:
            self.colorama = None

    def printc(self, text: str, color="Green") -> None:
        if self.colors_imported == True:
            match color:
                case "Green":
                    print(self.colorama.Fore.GREEN + str(text) + self.colorama.Fore.RESET)
                case "Red":
                    print(self.colorama.Fore.RED + str(text) + self.colorama.Fore.RESET)
                case "Yellow":
                    print(self.colorama.Fore.YELLOW + str(text) + self.colorama.Fore.RESET)
                case "Blue":
                    print(self.colorama.Fore.BLUE + str(text) + self.colorama.Fore.RESET)
                case "Magenta":
                    print(self.colorama.Fore.MAGENTA + str(text) + self.colorama.Fore.RESET)
                case "Cyan":
                    print(self.colorama.Fore.CYAN + str(text) + self.colorama.Fore.RESET)
        else:
            print(text)

    def inputc(self, text: str, color="Green") -> str:
        if self.colors_imported == True:
            match color:
                case "Green":
                    return input(self.colorama.Fore.GREEN + text + self.colorama.Fore.RESET)
                case "Red":
                    return input(self.colorama.Fore.RED + text + self.colorama.Fore.RESET)
                case "Yellow":
                    return input(self.colorama.Fore.YELLOW + text + self.colorama.Fore.RESET)
                case "Blue":
                    return input(self.colorama.Fore.BLUE + text + self.colorama.Fore.RESET)
                case "Magenta":
                    return input(self.colorama.Fore.MAGENTA + text + self.colorama.Fore.RESET)
                case "Cyan":
                    return input(self.colorama.Fore.CYAN + text)
        else:
            return input(text)