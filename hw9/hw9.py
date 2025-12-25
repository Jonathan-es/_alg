import json

def edit_distance(a, b):
    rows, cols = len(a), len(b)
    # Build the matrix
    m = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    for i in range(rows + 1): m[i][0] = i
    for j in range(cols + 1): m[0][j] = j

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
    return m

def get_alignment(a, b, m):
    i, j = len(a), len(b)
    res_a, res_b, markers = "", "", ""

    while i > 0 or j > 0:
        # Match
        if i > 0 and j > 0 and a[i-1] == b[j-1] and m[i][j] == m[i-1][j-1]:
            res_a = a[i-1] + res_a
            res_b = b[j-1] + res_b
            markers = "|" + markers
            i -= 1
            j -= 1
        # Substitution
        elif i > 0 and j > 0 and m[i][j] == m[i-1][j-1] + 1:
            res_a = a[i-1] + res_a
            res_b = b[j-1] + res_b
            markers = "." + markers
            i -= 1
            j -= 1
        # Deletion
        elif i > 0 and m[i][j] == m[i-1][j] + 1:
            res_a = a[i-1] + res_a
            res_b = "-" + res_b
            markers = " " + markers
            i -= 1
        # Insertion
        else:
            res_a = "-" + res_a
            res_b = b[j-1] + res_b
            markers = " " + markers
            j -= 1
    return res_a, markers, res_b

def save_markdown(a, b, matrix, alignment):
    dist = matrix[len(a)][len(b)]
    with open("README.md", "w") as f:
        f.write("# Assignment: Edit Distance\n\n")
        f.write(f"- **String A:** `{a}`\n")
        f.write(f"- **String B:** `{b}`\n")
        f.write(f"- **Distance:** {dist}\n\n")
        
        f.write("### Alignment\n```text\n")
        f.write(f"{alignment[0]}\n{alignment[1]}\n{alignment[2]}\n```\n\n")
        
        f.write("### DP Matrix\n")
        header = "| | | " + " | ".join(list(b)) + " |\n"
        f.write(header + "|" + "---|" * (len(b) + 2) + "\n")
        for r in range(len(matrix)):
            char = a[r-1] if r > 0 else "-"
            f.write(f"| {char} | " + " | ".join(map(str, matrix[r])) + " |\n")

if __name__ == "__main__":
    str_a = "ATGCAATCCC"
    str_b = "ATG ATCCG"
    
    matrix = edit_distance(str_a, str_b)
    alignment = get_alignment(str_a, str_b, matrix)
    
    # Terminal Display
    print(f"Edit Distance: {matrix[len(str_a)][len(str_b)]}")
    print(f"{alignment[0]}\n{alignment[1]}\n{alignment[2]}")
    
    save_markdown(str_a, str_b, matrix, alignment)
    print("\nFile 'README.md' has been created.")