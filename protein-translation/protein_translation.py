d = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "",
    "UAG": "",
    "UGA": "",
     }


def proteins(strand):
    i = 0
    res = []
    while i < len(strand):
        if len(d[strand[i:i+3]]) == 0:
            return res
        res.append(d[strand[i:i+3]])
        i += 3

    return res
