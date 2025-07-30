# rubiks_solver/cube/moves.py

import copy

VALID_MOVES = ['U', "U'", 'D', "D'", 'R', "R'", 'L', "L'", 'F', "F'", 'B', "B'"]

def rotate_face(face, times=1):
    # Rotate a face (list of 9) clockwise (times times)
    for _ in range(times % 4):
        face = [face[6], face[3], face[0],
                face[7], face[4], face[1],
                face[8], face[5], face[2]]
    return face

# Helper to swap slices among the affected edge stickers for each move:
def move_U(state):
    s = copy.deepcopy(state)
    s[0] = rotate_face(s[0])  # Up
    # U layer: swap edge triplets among F, R, B, L
    F, R, B, L = s[2], s[1], s[5], s[4]
    F0, R0, B0, L0 = F[:3], R[:3], B[:3], L[:3]
    F[:3], R[:3], B[:3], L[:3] = R0, B0, L0, F0
    return s

def move_Uprime(state):
    # U' = U x3
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_U(s)
    return s

def move_D(state):
    s = copy.deepcopy(state)
    s[3] = rotate_face(s[3])
    F, R, B, L = s[2], s[1], s[5], s[4]
    F3, R3, B3, L3 = F[6:], R[6:], B[6:], L[6:]
    F[6:], R[6:], B[6:], L[6:] = L3, F3, R3, B3
    return s

def move_Dprime(state):
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_D(s)
    return s

def move_R(state):
    s = copy.deepcopy(state)
    s[1] = rotate_face(s[1])
    U, F, D, B = s[0], s[2], s[3], s[5]
    # right column: U2-5-8, F2-5-8, D2-5-8, B6-3-0 (order reversed due to orientation)
    U2, U5, U8 = U[2], U[5], U[8]
    F2, F5, F8 = F[2], F[5], F[8]
    D2, D5, D8 = D[2], D[5], D[8]
    B6, B3, B0 = B[6], B[3], B[0]
    U[2], U[5], U[8] = B6, B3, B0
    F[2], F[5], F[8] = U2, U5, U8
    D[2], D[5], D[8] = F2, F5, F8
    B[6], B[3], B[0] = D2, D5, D8
    return s

def move_Rprime(state):
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_R(s)
    return s

def move_L(state):
    s = copy.deepcopy(state)
    s[4] = rotate_face(s[4])
    U, F, D, B = s[0], s[2], s[3], s[5]
    U0, U3, U6 = U[0], U[3], U[6]
    F0, F3, F6 = F[0], F[3], F[6]
    D0, D3, D6 = D[0], D[3], D[6]
    B8, B5, B2 = B[8], B[5], B[2]
    U[0], U[3], U[6] = F0, F3, F6
    F[0], F[3], F[6] = D0, D3, D6
    D[0], D[3], D[6] = B8, B5, B2
    B[8], B[5], B[2] = U0, U3, U6
    return s

def move_Lprime(state):
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_L(s)
    return s

def move_F(state):
    s = copy.deepcopy(state)
    s[2] = rotate_face(s[2])
    U, R, D, L = s[0], s[1], s[3], s[4]
    U6, U7, U8 = U[6], U[7], U[8]
    R0, R3, R6 = R[0], R[3], R[6]
    D2, D1, D0 = D[2], D[1], D[0]
    L8, L5, L2 = L[8], L[5], L[2]
    U[6], U[7], U[8] = L8, L5, L2
    R[0], R[3], R[6] = U6, U7, U8
    D[2], D[1], D[0] = R0, R3, R6
    L[8], L[5], L[2] = D2, D1, D0
    return s

def move_Fprime(state):
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_F(s)
    return s

def move_B(state):
    s = copy.deepcopy(state)
    s[5] = rotate_face(s[5])
    U, R, D, L = s[0], s[1], s[3], s[4]
    U0, U1, U2 = U[0], U[1], U[2]
    R2, R5, R8 = R[2], R[5], R[8]
    D8, D7, D6 = D[8], D[7], D[6]
    L6, L3, L0 = L[6], L[3], L[0]
    U[0], U[1], U[2] = R2, R5, R8
    R[2], R[5], R[8] = D8, D7, D6
    D[8], D[7], D[6] = L6, L3, L0
    L[6], L[3], L[0] = U0, U1, U2
    return s

def move_Bprime(state):
    s = copy.deepcopy(state)
    for _ in range(3):
        s = move_B(s)
    return s

# Map the move names to functions
MOVE_FUNCS = {
    'U': move_U,
    "U'": move_Uprime,
    'D': move_D,
    "D'": move_Dprime,
    'R': move_R,
    "R'": move_Rprime,
    'L': move_L,
    "L'": move_Lprime,
    'F': move_F,
    "F'": move_Fprime,
    'B': move_B,
    "B'": move_Bprime,
}
