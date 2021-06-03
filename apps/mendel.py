import pandas as pd

class PeriodicTable():
    """ Работаем с таблицой Менделеева
    Методы:
        elementByNumber(int)
        elementByNameRu(str)
        elementBySymbol(str)
    """

    def __init__(self):
        elements = [('AtomicNumber', 'Element', 'ElementRu', 'Symbol'),
                    (1, 'Hydrogen', 'Водород', 'H'),
                    (2, 'Helium', 'Гелий', 'He'),
                    (3, 'Lithium', 'Литий', 'Li'),
                    (4, 'Beryllium', 'Бериллий', 'Be'),
                    (5, 'Boron', 'Бор', 'B'),
                    (6, 'Carbon', 'Углерод', 'C'),
                    (7, 'Nitrogen', 'Азот', 'N'),
                    (8, 'Oxygen', 'Кислород', 'O'),
                    (9, 'Fluorine', 'Фтор', 'F'),
                    (10, 'Neon', 'Неон', 'Ne'),
                    (11, 'Sodium', 'Натрий', 'Na'),
                    (12, 'Magnesium', 'Магний', 'Mg'),
                    (13, 'Aluminum', 'Алюминий', 'Al'),
                    (14, 'Silicon', 'Кремний', 'Si'),
                    (15, 'Phosphorus', 'Фосфор', 'P'),
                    (16, 'Sulfur', 'Сера', 'S'),
                    (17, 'Chlorine', 'Хлор', 'Cl'),
                    (18, 'Argon', 'Аргон', 'Ar'),
                    (19, 'Potassium', 'Калий', 'K'),
                    (20, 'Calcium', 'Кальций', 'Ca'),
                    (21, 'Scandium', 'Скандий', 'Sc'),
                    (22, 'Titanium', 'Титан', 'Ti'),
                    (23, 'Vanadium', 'Ванадий', 'V'),
                    (24, 'Chromium', 'Хром', 'Cr'),
                    (25, 'Manganese', 'Марганец', 'Mn'),
                    (26, 'Iron', 'Железо', 'Fe'),
                    (27, 'Cobalt', 'Кобальт', 'Co'),
                    (28, 'Nickel', 'Никель', 'Ni'),
                    (29, 'Copper', 'Медь', 'Cu'),
                    (30, 'Zinc', 'Цинк', 'Zn'),
                    (31, 'Gallium', 'Галлий', 'Ga'),
                    (32, 'Germanium', 'Германий', 'Ge'),
                    (33, 'Arsenic', 'Мышьяк', 'As'),
                    (34, 'Selenium', 'Селен', 'Se'),
                    (35, 'Bromine', 'Бром', 'Br'),
                    (36, 'Krypton', 'Криптон', 'Kr'),
                    (37, 'Rubidium', 'Рубидий', 'Rb'),
                    (38, 'Strontium', 'Стронций', 'Sr'),
                    (39, 'Yttrium', 'Иттрий', 'Y'),
                    (40, 'Zirconium', 'Цирконий', 'Zr'),
                    (41, 'Niobium', 'Ниобий', 'Nb'),
                    (42, 'Molybdenum', 'Молибден', 'Mo'),
                    (43, 'Technetium', 'Технеций', 'Tc'),
                    (44, 'Ruthenium', 'Рутений', 'Ru'),
                    (45, 'Rhodium', 'Родий', 'Rh'),
                    (46, 'Palladium', 'Палладий', 'Pd'),
                    (47, 'Silver', 'Серебро', 'Ag'),
                    (48, 'Cadmium', 'Кадмий', 'Cd'),
                    (49, 'Indium', 'Индий', 'In'),
                    (50, 'Tin', 'Олово', 'Sn'),
                    (51, 'Antimony', 'Сурьма', 'Sb'),
                    (52, 'Tellurium', 'Теллур', 'Te'),
                    (53, 'Iodine', 'Иод', 'I'),
                    (54, 'Xenon', 'Ксенон', 'Xe'),
                    (55, 'Cesium', 'Цезий', 'Cs'),
                    (56, 'Barium', 'Барий', 'Ba'),
                    (57, 'Lanthanum', 'Лантан', 'La'),
                    (58, 'Cerium', 'Церий', 'Ce'),
                    (59, 'Praseodymium', 'Празеодим', 'Pr'),
                    (60, 'Neodymium', 'Неодим', 'Nd'),
                    (61, 'Promethium', 'Прометий', 'Pm'),
                    (62, 'Samarium', 'Самарий', 'Sm'),
                    (63, 'Europium', 'Европий', 'Eu'),
                    (64, 'Gadolinium', 'Гадолиний', 'Gd'),
                    (65, 'Terbium', 'Тербий', 'Tb'),
                    (66, 'Dysprosium', 'Диспрозий', 'Dy'),
                    (67, 'Holmium', 'Гольмий', 'Ho'),
                    (68, 'Erbium', 'Эрбий', 'Er'),
                    (69, 'Thulium', 'Тулий', 'Tm'),
                    (70, 'Ytterbium', 'Иттербий', 'Yb'),
                    (71, 'Lutetium', 'Лютеций', 'Lu'),
                    (72, 'Hafnium', 'Гафний', 'Hf'),
                    (73, 'Tantalum', 'Тантал', 'Ta'),
                    (74, 'Wolfram', 'Вольфрам', 'W'),
                    (75, 'Rhenium', 'Рений', 'Re'),
                    (76, 'Osmium', 'Осмий', 'Os'),
                    (77, 'Iridium', 'Иридий', 'Ir'),
                    (78, 'Platinum', 'Платина', 'Pt'),
                    (79, 'Gold', 'Золото', 'Au'),
                    (80, 'Mercury', 'Ртуть', 'Hg'),
                    (81, 'Thallium', 'Таллий', 'Tl'),
                    (82, 'Lead', 'Свинец', 'Pb'),
                    (83, 'Bismuth', 'Висмут', 'Bi'),
                    (84, 'Polonium', 'Полоний', 'Po'),
                    (85, 'Astatine', 'Астат', 'At'),
                    (86, 'Radon', 'Радон', 'Rn'),
                    (87, 'Francium', 'Франций', 'Fr'),
                    (88, 'Radium', 'Радий', 'Ra'),
                    (89, 'Actinium', 'Актиний', 'Ac'),
                    (90, 'Thorium', 'Торий', 'Th'),
                    (91, 'Protactinium', 'Протактиний', 'Pa'),
                    (92, 'Uranium', 'Уран', 'U'),
                    (93, 'Neptunium', 'Нептуний', 'Np'),
                    (94, 'Plutonium', 'Плутоний', 'Pu'),
                    (95, 'Americium', 'Америций', 'Am'),
                    (96, 'Curium', 'Кюрий', 'Cm'),
                    (97, 'Berkelium', 'Берклий', 'Bk'),
                    (98, 'Californium', 'Калифорний', 'Cf'),
                    (99, 'Einsteinium', 'Эйнштейний', 'Es'),
                    (100, 'Fermium', 'Фермий', 'Fm'),
                    (101, 'Mendelevium', 'Менделевий', 'Md'),
                    (102, 'Nobelium', 'Нобелий', 'No'),
                    (103, 'Lawrencium', 'Лоуренсий', 'Lr'),
                    (104, 'Rutherfordium', 'Резерфордий', 'Rf'),
                    (105, 'Dubnium', 'Дубний', 'Db'),
                    (106, 'Seaborgium', 'Сиборгий', 'Sg'),
                    (107, 'Bohrium', 'Борий', 'Bh'),
                    (108, 'Hassium', 'Хассий', 'Hs'),
                    (109, 'Meitnerium', 'Мейтнерий', 'Mt'),
                    (110, 'Darmstadtium ', 'Дармштадтий', 'Ds '),
                    (111, 'Roentgenium ', 'Рентгений', 'Rg '),
                    (112, 'Copernicium ', 'Коперниций', 'Cn '),
                    (113, 'Nihonium', 'Нихоний', 'Nh'),
                    (114, 'Flerovium', 'Флеровий', 'Fl'),
                    (115, 'Moscovium', 'Московий', 'Mc'),
                    (116, 'Livermorium', 'Ливерморий', 'Lv'),
                    (117, 'Tennessine', 'Теннессин', 'Ts'),
                    (118, 'Oganesson', 'Оганесон', 'Og'),
                    ]
        self.periodicTableData = pd.DataFrame(elements[1:], columns=elements[0])
        # self.periodicTableData = self.periodicTableData.set_index('AtomicNumber')

    def elementByNumber(self, number):
        df = self.periodicTableData
        if type(number) != 'int':
            try:
                number = int(number)
            except:
                return f'Error: {number} is not an element number'
        if 1 <= number <= 118:
            return df.loc[df['AtomicNumber'] == number].values[0]
        else:
            return f'Error: element number {number} does not exist'

    def elementByNameRu(self, name):
        df = self.periodicTableData
        if df.loc[df['ElementRu'].str.upper() == name.upper()].values.any():
            return df.loc[df['ElementRu'].str.upper() == name.upper()].values[0]
        else:
            return ['','','','']

    def elementBySymbol(self, symbol):
        df = self.periodicTableData
        if df.loc[df['Symbol'].str.upper() == symbol.upper()].values.any():
            return df.loc[df['Symbol'].str.upper() == symbol.upper()].values[0]
        else:
            return ['','','','']

if __name__ == '__main__':
    mendel = PeriodicTable()
    print(mendel.elementByNumber(8))
    print(mendel.elementByNameRu('сера1'))
    print(mendel.elementBySymbol('ti'))