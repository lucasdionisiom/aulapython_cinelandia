senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"digite a senha (Tentativa {tentativas +1}/{max_tentativas}): ")
    if tentativa == senha_correta:
        print("acesso concedido! Bem-vindo.")
        break
    else:
        print("Senha incorreta")
        tentativas += 1

else:
    print("voce excedeu o numero maximo de tentativas. Acesso bloqueado.")