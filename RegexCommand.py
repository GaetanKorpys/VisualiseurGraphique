class RegexCommand():
    def __init__(self):
        # REGEX COMMAND
        self.avancerRegex = "^AVANCE (?:[1-9]|[1-9][0-9]|[1-4][0-9]{2}|500)$"
        self.reculerRegex = "^RECULE (?:[1-9]|[1-9][0-9]|[1-4][0-9]{2}|500)$"
        self.tourneDroiteRegex = "^TOURNEDROITE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$"
        self.tourneGaucheRegex = "^TOURNEGAUCHE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$"
        self.leveCrayonRegex = "^LEVECRAYON$"
        self.baisseCrayonRegex = "^BAISSECRAYON$"
        self.origineRegex = "^ORIGINE$"
        self.restaureRegex = "^RESTAURE$"
        self.nettoieRegex = "^NETTOIE$"
        self.fccRegex = "^FCC (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$"
        self.fcapRegex = "^FCAP (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$"
        self.fposRegex = "^FPOS \[(?:[1-4]\d{0,2}|500|\d{1,2}) (?:[1-4]\d{0,2}|500|\d{1,2})\]$"
        self.repetRegex = "^REPETE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9]) \[$"