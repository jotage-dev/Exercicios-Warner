def movimento_valido_cavalo(x_atual, y_atual, x_destino, y_destino):
    limite_valido = lambda v: 0 <= v <= 7
    if not (limite_valido(x_atual) and limite_valido(y_atual) and limite_valido(x_destino) and limite_valido(y_destino)):
        return False

    delta_x = abs(x_destino - x_atual)
    delta_y = abs(y_destino - y_atual)

    padroes_l = {(1, 2), (2, 1)}
    return (delta_x, delta_y) in padroes_l

if __name__ == "__main__":
    # Bateria de testes
    casos_de_teste = [
        (5, 2, 6, 4, True),
        (5, 2, 3, 3, True),
        (5, 2, 7, 3, True),
        (5, 2, 4, 0, True),
        (5, 2, 5, 4, False),
        (5, 2, 6, 3, False),
        (5, 2, 5, 5, False),
        (5, 2, 9, 9, False),
        (5, 2, -1, 1, False),
        (-2, -1, 0, 0, False),
    ]

    acertos = 0
    print("=== Testes de Movimentação do Cavalo ===")
    for x1, y1, x2, y2, valor_esperado in casos_de_teste:
        resultado = movimento_valido_cavalo(x1, y1, x2, y2)
        passou = (resultado == valor_esperado)
        
        if passou:
            acertos += 1
            
        status_txt = "PASSOU" if passou else "FALHOU"
        print(f"[{status_txt}] Origem({x1},{y1}) -> Destino({x2},{y2}) | Resultado: {resultado}")

    print(f"\nResumo: {acertos} de {len(casos_de_teste)} testes passaram com sucesso.")
