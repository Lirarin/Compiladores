
OPERATORS = ['*', '+', '-', '*', '/'] # Conjunto de operadores passado na atividade
DIGITS = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9'] # Conjunto de algarismos passado na atividade
SPECIAL_DIGITS = ['x', 'y', 'z', 't','w','X', 'Y', 'Z','T','W']# Conjunto de tokems atomicos passado na atividade
SPECIAL_OPERATORS = ['@', '!', '#',]# Conjunto de caracteres especiais Diferentes de Parenteses,Colchetes e chaves
LPARENT = ['(']
RPARENT = [')']
LSQUAREBRKT = ['[']
RSQUAREBRKT = [']']
LCURLYBRKT = ['{']
RCURLYBRKT = ['}']
OPENFACTOR = [LPARENT, LSQUAREBRKT, LCURLYBRKT]# Conjunto de caracteres Parenteses,Colchetes e chaves de abertura 
CLOSEFACTOR = [RPARENT, RSQUAREBRKT, RCURLYBRKT]# Conjunto de caracteres Parenteses,Colchetes e chaves de fechamento

test = "{x+1[-3][52+(4*t)]/14}-10" # exemplo de expressão balanceada para testes

string = input() # captura input
palavra =string[:10] # limita input a 10 caracteres

def is_bracket_closed(string): # função que checa se o parenteses está fechado ou aberto
    bracket_stack = [] # pilha de parenteses

    for bracket in string: # roda a string, se achar um parenteses de abertura, empilha
        if bracket in OPENFACTOR:
            bracket_stack.append(bracket)

        elif bracket in CLOSEFACTOR: 
            # roda a sting, se achar um parênteses fechamento, e não tiver parenteses de abertura ou tiver o tipo errado de parenteses de abertura e fechadura retorna falso
            if len(bracket_stack) == 0: # se não achar nada, falso
                return False
            popped_bracket = bracket_stack.pop()
            if not brackets_correspond(popped_bracket, bracket): # roda a string e checa se o parenteses indicado está de acordo com os empilhados
                return False
                
    if len(bracket_stack) != 0: # se tiver rodado a pilha e tinha algo que não caiu em condições acima, falso(bugfix)
        return False
    return True

def brackets_correspond(opening, closing):# roda a string e checa se o parenteses indicado está de acordo com os empilhados
    if opening == '(' and closing == ')':
        return True
    if opening == '{' and closing == '}':
        return True
    if opening == '[' and closing == ']':
        return True
    return False

def is_operator_alternated(string):# checa se os operadores estão alternados
    previous = None
    for character in string:
        if character in OPERATORS:
            if previous in ('*', '+', '-', '/'):
                return False
        previous = character
    return True

def is_expression(string): # checa se é expressão numérica ou não
    for index, character in enumerate(string): # percorre cada caractere
        if character in SPECIAL_DIGITS: # se achar um Caractere Especial
            before = string[index - 1] if index - 1 >= 0 else None # le o digito anterior
            after = string[index + 1] if index + 1 < len(string) else None # le o digito posterior
            if after not in SPECIAL_DIGITS and before not in SPECIAL_DIGITS:# checa se o caractere da posição anterior também era dígito(não alternado)
                return True
    return False

def has_SPECIAL(string): # checa novamente se há caracteres especiais(bugFix)
    for index, character in enumerate(string):
        if character in SPECIAL_DIGITS:
            return True
        break
    return False

if palavra[0].isdigit(): # se a palavra começa com algarismos romanos
    print("Palavra resevada")
else:
    if is_bracket_closed(palavra) == True and is_operator_alternated(palavra) == True and is_expression(palavra) == True: 
        # se parenteses estao corretos, operadores alternados, e os digitos especiais estão no formato correto, é uma expressão matemática
        print("É uma expressão matemática")
    elif is_expression(palavra) == False and has_SPECIAL == False:
        # se não tem formato de expressão e também não tem digitos especiais, é uma string
        print("É uma string")
    else: print("Palavra não aceita") # caso falhe nas condições acima, não é aceita
