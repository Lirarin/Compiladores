def remove_lambda_rules(grammar):
    has_lambda = True
    while has_lambda:
        has_lambda = False
        for variable, productions in grammar.items():
            if 'λ' in productions:
                productions.remove('λ')
                if len(productions) == 0:
                    grammar[variable] = ['λ']
                has_lambda = True
            else:
                for production in productions:
                    if all(symbol in grammar.keys() for symbol in production):
                        for symbol in production:
                            if symbol in grammar and 'λ' in grammar[symbol]:
                                new_production = list(production)
                                new_production.remove(symbol)
                                new_production.extend(grammar[symbol])
                                if new_production not in productions:
                                    productions.append(new_production)
                                has_lambda = True
    return grammar


def eliminate_unit_rules(grammar):
    unit_rules = [(variable, production[0]) for variable, productions in grammar.items()
                    for production in productions if len(production) == 1 and production[0] in grammar.keys()]

    for A, B in unit_rules:
        grammar[A].remove(B)
        grammar[A].extend(grammar[B])

    return grammar


def eliminate_useless_variables(grammar):
    start_symbol = 'S'
    reachable = set(start_symbol)
    changed = True
    while changed:
        changed = False
        for variable, productions in grammar.items():
            if variable in reachable:
                for production in productions:
                    for symbol in production:
                        if symbol in grammar.keys() and symbol not in reachable:
                            reachable.add(symbol)
                            changed = True

    for variable in list(grammar.keys()):
        if variable not in reachable:
            del grammar[variable]

    return grammar


def rename_variables(grammar):
    nonterminals = list(grammar.keys())
    renamed_variables = {nonterminal: 'A' + str(i + 1) for i, nonterminal in enumerate(nonterminals)}

    renamed_grammar = {}

    for nonterminal, variable in renamed_variables.items():
        productions = grammar[nonterminal]
        renamed_productions = []

        for production in productions:
            renamed_production = []
            for symbol in production:
                if symbol in nonterminals:
                    renamed_production.append(renamed_variables[symbol])
                else:
                    renamed_production.append(symbol)
            renamed_productions.append(''.join(renamed_production))

        renamed_grammar[variable] = renamed_productions

    return renamed_grammar


def convert_to_greibach(grammar):
    grammar = remove_lambda_rules(grammar)
    grammar = eliminate_unit_rules(grammar)
    grammar = eliminate_useless_variables(grammar)
    grammar = rename_variables(grammar)

    converted_grammar = {}

    for nonterminal, productions in grammar.items():
        converted_productions = []

        for production in productions:
            converted_production = []
            for symbol in production:
                if symbol.isupper():
                    converted_production.append(symbol)
                else:
                    converted_production.append("'" + symbol + "'")
            converted_productions.append(''.join(converted_production))

        converted_grammar[nonterminal] = converted_productions

    return converted_grammar


grammar = {
    'S': ['aAd', 'A'],
    'A': ['Bc', 'λ'],
    'B': ['Ac', 'a']
}

converted_grammar = convert_to_greibach(grammar)

for nonterminal, productions in converted_grammar.items():
    for production in productions:
        print(f'{nonterminal} -> {production}')
