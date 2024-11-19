import random

#  9x9 boş bir Sudoku tahtası
sudoku_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()

def is_valid_move(board, row, col, num):
    # Satırda num olup olmadığını kontrol et
    if num in board[row]:
        return False
    # Sütunda num olup olmadığını kontrol et
    for i in range(9):
        if board[i][col] == num:
            return False
    # 3x3 kutuda num olup olmadığını kontrol et
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def fill_board(board):
    # Rastgele olarak tahtanın bazı hücrelerini doldur
    num_filled = 0
    while num_filled < 20:  # 20 hücreyi rastgele doldur
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid_move(board, row, col, num):
            board[row][col] = num
            num_filled += 1

def play_sudoku():
    fill_board(sudoku_board)
    print("Sudoku oyununa hoş geldiniz!")
    print_board(sudoku_board)

    while True:
        try:
            row = int(input("Satır (1-9): ")) - 1
            col = int(input("Sütun (1-9): ")) - 1
            num = int(input("Sayı (1-9): "))

            if sudoku_board[row][col] != 0:
                print("Bu hücre zaten dolu! Başka bir hücre seçin.")
                continue

            if is_valid_move(sudoku_board, row, col, num):
                sudoku_board[row][col] = num
                print_board(sudoku_board)
                
                # Tüm hücreler dolduysa oyunu bitir
                if all(all(cell != 0 for cell in row) for row in sudoku_board):
                    print("Tebrikler! Sudoku'yu tamamladınız!")
                    break
            else:
                print("Geçersiz hareket! Tekrar deneyin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen 1-9 arasında bir sayı girin.")

# Oyunu başlat
play_sudoku()
