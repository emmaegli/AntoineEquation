import pandas


def antoine_equation(A: int, B: int, C: int, T: int) -> int:
    return 10 ** (A - (B / (C + T)))


excel = pandas.read_excel("table.xlsx")

print(excel)

# Get user input to define variables

chemical_name = input(
    "What chemical do you want to search? It can be a compound name or molecular formula.\n"
)
temperature = int(input("Enter temperature (degree celsius) to evaluate at.\n"))

chemical_name = chemical_name.lower()  # lowercase the user input chemical name

table_chemicals = [
    chemical.lower() for chemical in excel["Name"].tolist()
]  # make the raw table lowercase
table_formulas = [
    formula.lower() for formula in excel["Formula"].tolist()
]  # make the raw table lowercase

try:
    rownum = (
        table_chemicals.index(chemical_name)
        if chemical_name in table_chemicals
        else table_formulas.index(chemical_name)
    )
except ValueError:
    raise Exception("The chemical entered is not on the list")

row = excel.iloc[rownum].tolist()

print(
    antoine_equation(row[2], row[3], row[4], temperature)
)  # this is the p_sat value from the Antoine Equation in mmHg
