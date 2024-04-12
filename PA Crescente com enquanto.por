// PA crescente com enquanto
// 12/04/2024
// Autor: Raphael Ferraz


programa
{
	
	funcao inicio()
	{
		inteiro numero, resultado, contador
		
		escreva("Digite um número para ver sua sequencia: ")
		leia(numero)

		contador = 1
		
		enquanto ( contador <= 20 ) 
		{
			resultado = numero + contador 
			escreva (numero, " - ", contador, " = ", resultado , "\n")
		 	contador++
		}
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 291; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */