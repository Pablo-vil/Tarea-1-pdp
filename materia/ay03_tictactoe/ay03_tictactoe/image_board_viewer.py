from board import Board
from board_view import BoardView
from PIL import Image, ImageDraw, ImageFont


class ImageBoardView(BoardView):

    def display(self, board: Board) -> None:
        size: int = board.size()
        # Crear una imagen con fondo blanco
        side_size: int = size*100
        board_image = Image.new('RGB', (side_size, side_size), 'white')

        # Crear objeto para dibujar
        board_draw = ImageDraw.Draw(board_image)
        
        # Dibujamos las líneas verticales y horizontales
        for i in range(size - 1):
            board_draw.line(((i+1)*side_size/size, 0, (i+1)*side_size/size, side_size), 
                            fill='black', width=4)
            board_draw.line((0, (i+1)*side_size/size, side_size, (i+1)*side_size/size), 
                            fill='black', width=4)
            
        # Pintamos los símbolos de cada jugador
        # Obtenemos una fuente (en este caso directo desde un archivo)
        font = ImageFont.truetype("arial.ttf", 48)
        for row in range(size):
            for col in range(size):
                cell = board.cell_state(row, col)
                if cell is not None:
                    # Definimos la posición donde debemos escribir el símbolo
                    xy = (col*side_size/size + side_size/(2*size), 
                          row*side_size/size + side_size/(2*size))
                    # El anchor define como se escribe relativo a la posición
                    # en este caso mm es midle-midle (centrado)
                    board_draw.text(xy, cell.get_symbol(), 
                                    fill=cell.get_color(), font=font, anchor="mm")

        # Mostramos la imagen generada
        board_image.show()
