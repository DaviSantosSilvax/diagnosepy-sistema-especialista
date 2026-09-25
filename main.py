def obter_input_usuario():
    """
    Simula a entrada do usuário para o tipo de erro, conforme o fluxograma.
    No fluxograma, o usuário informa as informações sobre o erro.
    """
    print("--- Sistema Especialista para Diagnóstico de Erros de Programação ---")
    print("Tipos de erros contemplados:")
    print("1. SyntaxError")
    print("2. NameError")
    print("3. TypeError")
    print("4. ValueError")
    print("5. IndexError")
    print("6. KeyError")
    print("7. ZeroDivisionError")
    print("8. IndentationError")
    print("9. ImportError")
    print("10. Erro de Lógica")
    
    while True:
        try:
            opcao = int(input("\nDigite o número correspondente ao tipo de erro ou '0' para sair: "))
            
            mapeamento_erros = {
                1: "SyntaxError",
                2: "NameError",
                3: "TypeError",
                4: "ValueError",
                5: "IndexError",
                6: "KeyError",
                7: "ZeroDivisionError",
                8: "IndentationError",
                9: "ImportError",
                10: "Erro de Lógica",
                0: "Sair"
            }
            
            if opcao in mapeamento_erros:
                return mapeamento_erros[opcao]
            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida. Digite um número.")

def motor_inferencia(tipo_erro):
    """
    Atua como o Motor de Inferência do fluxograma, analisando o tipo de erro
    e consultando a Base de Conhecimento (regras embutidas).
    """
    
    # Base de Conhecimento (regras mapeadas)
    # Cada chave corresponde a um tipo de erro e o valor é uma tupla com (Possível causa, Orientação/Solução)
    base_conhecimento = {
        "SyntaxError": ("Estrutura do código incorreta.", 
                        "Verifique a sintaxe: pontuação (parênteses, colchetes, chaves), dois pontos ':', e palavras-chave."),
        "NameError": ("Variável ou função não definida.", 
                      "Verifique se o nome da variável ou função foi digitado corretamente e se ela foi criada e inicializada antes de ser usada."),
        "TypeError": ("Tipo de dado incompatível.", 
                       "Verifique se você está realizando operações com tipos de dados adequados (ex: somar uma string com um número)."),
        "ValueError": ("Valor inválido para a operação.", 
                        "Verifique se o valor passado para uma função ou operação é válido (ex: tentar converter 'texto' para 'int')."),
        "IndexError": ("Índice fora dos limites da lista.", 
                        "Verifique o tamanho da lista e o índice que você está tentando acessar."),
        "KeyError": ("Chave inexistente no dicionário.", 
                      "Verifique se a chave solicitada existe no dicionário."),
        "ZeroDivisionError": ("Divisão por zero.", 
                              "Verifique se o divisor em uma operação de divisão pode ser zero."),
        "IndentationError": ("Problema na indentação do código.", 
                               "Verifique os espaços ou tabs no início das linhas de código."),
        "ImportError": ("Módulo não encontrado ou import incorreto.", 
                         "Verifique se o nome do módulo está correto e se ele está instalado."),
        "Erro de Lógica": ("Condição, laço ou variável incorreta.", 
                            "Verifique se a lógica do seu código está correta: condições, laços (for, while) e o valor das variáveis.")
    }
    
    # Regra correspondente (Decisão no fluxograma)
    if tipo_erro in base_conhecimento:
        causa, orientacao = base_conhecimento[tipo_erro]
        return causa, orientacao
    elif tipo_erro == "Sair":
        return None, None
    else:
        # No fluxograma, esse caso seria tratado como "Erro não contemplado"
        return "Erro não contemplado na base de conhecimento.", "Verifique a mensagem de erro detalhada e o código."

def exibir_diagnostico_final(tipo_erro, causa, orientacao):
    """
    Atua como a etapa 'Exibir diagnóstico final' do fluxograma.
    """
    print("\n--- Diagnóstico Final ---")
    print(f"Tipo de erro: {tipo_erro}")
    print(f"Possível causa: {causa}")
    print(f"Orientação: {orientacao}")
    print("-" * 25)

def main():
    while True:
        # Etapa: Início e Entrada do Usuário
        tipo_erro_informado = obter_input_usuario()
        
        if tipo_erro_informado == "Sair":
            print("\nEncerrando o Sistema Especialista. Até logo!")
            break
            
        # Etapa: Motor de Inferência (Análise e Decisão)
        causa, orientacao = motor_inferencia(tipo_erro_informado)
        
        # Etapa: Exibir diagnóstico final
        if causa and orientacao:
            exibir_diagnostico_final(tipo_erro_informado, causa, orientacao)
        
        # Etapa: Decisão "O usuário deseja ver mais detalhes ou outra análise?"
        continuar = input("\nDeseja realizar outra análise? (s/n): ").lower()
        if continuar != 's':
            print("\nEncerrando o Sistema Especialista. Até logo!")
            break

if __name__ == "__main__":
    main()