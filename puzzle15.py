import turtle
import tkinter as tk
import random

NumFilas = 4
NumCols = 4
Wd = 90
Hg = 90
FSz = 24
FONT = ('Helvetica', FSz, 'normal')

def crear_tiles():
	board = [["#" for _ in range (NumCols)] for _ in range (NumFilas)]
	num = 1
	for i in range (NumFilas):
		for j in range (NumCols):
			if num == NumFilas * NumCols:
				tile = turtle.Turtle()
				tile.penup()
				tile.hideturtle()
				board[i][j] = tile
			else:
				tile = turtle.Turtle()
				tile.penup()
				tile.goto(-138 + j * (Wd + 2), 138 -i * (Hg +2))
				tile.write(str(num), align="center", font=FONT)
				board[i][j] = tile
				num += 1
	return board

def encontrar_void():
	global board
	for fila in range (NumFilas):
		for columnas in range (NumCols):
			if board[fila][columnas].write()== "":
				return fila,columnas


def index_2d(lista, v):
	for i, x in enumerate(lista):
		if v in x:
			return (i, x.index(v))

def es_adyacente(el1, el2):
	return abs(el2[0] - el1[0]) == 1

def dibujar_board():
	global screen, board
	screen.tracer(0)
	for i in range (NumFilas):
		for j in range (NumCols):
			board[i][j].showturtle()
	screen.tracer(1)

def cambiar_tile(tile):
	global board
	vacio_i, vacio_j = encontrar_void()
	actual_i, actual_j = index_2d(board, tile)
	if es_adyacente([actual_i, actual_j], [vacio_i][vacio_j]):
		board[vacio_i][vacio_j], board[actual_i][actual_j] = board[actual_i][actual_j], board[vacio_i][vacio_j]
		dibujar_board()


def main():
	global screen, board
	screen = turtle.Screen()
	screen.setup(600, 600)
	screen.title("15 Puzzle")
	screen.bgcolor("aliceblue")
	screen.tracer(0)
	board = crear_tiles()
	screen.exitonclick()
if __name__ == "__main__":
	main()

turtle.done()