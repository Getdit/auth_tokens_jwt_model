
def menu(title, classes):

    print(title)
    for x, y in enumerate(classes):
        print(f"    {x}) {y}")

    return int(input("\n Digite o número da opção escolhida: "))

