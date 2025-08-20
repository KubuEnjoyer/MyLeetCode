# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
from collections import defaultdict

def zeroFilledSubarray(nums: list[int]) -> int:
    """
    Calcola il numero totale di sottoarray composti esclusivamente da zeri.

    Logica:
    - Si scorre l’array tenendo un contatore `length` che misura la lunghezza
      della sequenza di zeri consecutivi incontrata.
    - Quando si incontra un numero diverso da zero, si salva in `subarray_map`
      quante sequenze di quella lunghezza sono state trovate e si azzera `length`.
    - Dopo il ciclo, si aggiunge l’ultima sequenza (se presente).
    - Per ogni lunghezza `i` trovata, il numero di sottoarray di soli zeri che
      si possono formare è dato dalla formula: i*(i+1)/2.
      (es: per una sequenza di 3 zeri ⇒ 6 sottoarray: [0], [0], [0], [0,0], [0,0], [0,0,0])
    - Si moltiplica il risultato per quante volte quella lunghezza compare e si
      somma a `num`.
    - Si ritorna `num` convertito a intero, perché la divisione produce float.
    """
    num = 0
    subarray_map = defaultdict(int)
    length = 0
    for i in nums:
        if i == 0:
            length += 1
        else:
            subarray_map[length] += 1
            length = 0
    subarray_map[length] += 1
    for i, j in subarray_map.items():
        num += (i*(i+1))/2*j
    return int(num)

lista = [0,0,0,2,0,0]
print(zeroFilledSubarray(lista))

# Questa funzione è facilemente ottimizabile ma questa è la prima soluzione che mi è venuta in mente