
def maxArea(height: list[int]) -> int:
    """
    Data una lista di altezze (height), rappresentanti linee verticali su un grafico,
    bisogna trovare due linee che, insieme all’asse x, formino un contenitore capace
    di contenere la massima quantità d’acqua.

    Logica:
    - Si usano due puntatori: `i` all’inizio e `j` alla fine dell’array.
    - L’area del contenitore è calcolata come:
        min(height[i], height[j]) * (j - i)
      (altezza limitata dalla linea più bassa × distanza tra le due linee).
    - Ad ogni passo si sposta il puntatore che punta alla linea più bassa:
        * se height[i] < height[j] → si incrementa `i`
        * altrimenti → si decrementa `j`
      Questo perché la capacità è limitata dalla linea più corta, quindi conviene
      provare a spostarla per cercare un contenitore più alto.
    - Si aggiorna la massima area trovata (`A`) se quella corrente è maggiore.
    - Il ciclo termina quando i due puntatori si incontrano.
    - Infine, si ritorna `A`, la massima area trovata.
    """
    i = 0
    j = len(height)-1
    A = min(height[i], height[j])*(j-i)
    while i != j:
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        if A < min(height[i], height[j])*(j-i):
            A = min(height[i], height[j])*(j-i)
    return A

h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))

