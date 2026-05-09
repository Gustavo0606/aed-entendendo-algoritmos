from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    pilhaTeste = MyStack()
    if len(string) == 0:
        return True
    if string[0] == ")" or string[0] == "]" or string[0] == "}":
        return False
    for i in range(len(string)):
        parentese = string[i]
        if parentese in "([{":
            pilhaTeste.push(parentese)
        elif parentese in ")}]":
            if pilhaTeste.is_empty():
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
    return pilhaTeste.is_empty()
