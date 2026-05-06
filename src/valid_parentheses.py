# from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    pilhaTeste = []
    if len(string) == 0:
        return True
    if string[0] == ")" or string[0] == "]" or string[0] == "}":
        return False
    for i in range(len(string)):
        parentese = string[i]
        if parentese in "([{":
            pilhaTeste.append(parentese)
        elif parentese in ")}]":
            if not pilhaTeste:
                return False
            removido = pilhaTeste.pop()
            if parentese == ")" and removido != "(":
                return False
            if parentese == "]" and removido != "[":
                return False
            if parentese == "}" and removido != "{":
                return False
        else:
            return False
    if len(pilhaTeste) == 0:
        return True
    else:
        return False
