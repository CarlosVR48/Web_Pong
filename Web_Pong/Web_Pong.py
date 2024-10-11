from rxconfig import config
import reflex as rx
from views.navbar import navbar

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("-Crea tu propia máquina", size="8"),
            color="black",
            aling="center",
            justify="center",
            min_height="20vh",
            padding_y="1%",
        ),
        
        rx.vstack(    
            rx.image(src="pong_01.png",alt="Maquina de pong Arduino UNO",width="470px", height="300px"),
            rx.image(src="pong_02.png",alt="Maquina de pong Arduino UNO",width="470px", height="300px"),
            spacing="3",
            align="center",
            min_height="35vh",
            padding_x="1%",
            position="sticky"
        ),
        
        rx.vstack( 
            rx.text(
                "El proyecto ha sido construido con el Arduino Uno. Conexión RCA de línea de video y de sonido. Interruptor para seleccionar 2 modalidades de juego.", size="5"),
            rx.list.ordered(
                rx.list.item("UN PLAYER - FRONTON"),
                rx.list.item("DOS PLAYERS - PONG"),
                color="red",
                aling="start,"
            ),
            rx.text(
                "El repositorio del programa de pong del Arduino UNO, se encuentra en el enlace de gitHub de aquí abajo.", size="5"),
            color="black",
            direction="column",
            spacing="5",
            justify="center",
            min_height="30vh",
            padding_y="10px"
        ),       

        rx.hstack(
            rx.link(
                rx.button(rx.icon(tag="atom"),"gitHub",
                        color_scheme="red",
                        border_radius="2em",
                        box_sizing="border-box",
                        color="withe"),

                href="https://github.com/CarlosVR48/Arduino-Pong/",
                is_external=True,
                weight="medium",
                trim="normal"
            ),        
            rx.image(src="github.png",alt="gitHub",width="64", height="25"),
            direction="row",
            align="center",
            padding_x="25%",
            padding_y="15%",
        ),

        rx.vstack( 
            rx.text("Los siguientes videos, son el ejemplo de funcionamiento de la máquina. En el primero se ve cómo funcionan los mandos y en el segundo el funcionamiento del juego Ping Pong.",size="5"),
            color="black",
            direction="column",
            justify="center",
            min_height="15vh",
            paddig_y="10px",
        ), 

        rx.hstack( 
            rx.video(
               url="/pong_01.mp4",
               width="400px",
               height="200px",
               controls=True
            ),
            rx.video(
               url="/pong_02.mp4",
               width="400px",
               height="200px",
               controls=True,
            ),
            direction="row",
            spacing="5",
            justify="center",
            min_height="35vh"
        ),
       

        rx.vstack( 
            rx.text("Intenta representar la maravillosa máquina de videojuegos de Atari Pong, a la que hemos jugado casi todos, aunque algunos fuera un clon. La primera máquina se llamó Tele-Games Pong (1975) y la segunda Atari Pong (1976). En el siguiente enlace de la wiki dejo un poco de historia.",size="5"),
            color="black",
            direction="column",
            justify="center",
            min_height="15vh",
            paddig_y="10px",
        ), 

        rx.hstack(     
            rx.link(
                rx.button(rx.icon(tag="book_lock"),"Wikipedia",
                          color_scheme="red",
                        border_radius="2em",
                        box_sizing="border-box",
                        color="withe"),
                href="https://es.wikipedia.org/wiki/Atari_Pong",
                is_external=True,
                direction="row",
                weight="medium",
                trim="normal"
            ),
            rx.image(src="pong1.png",alt="Maquina de pong Atari",width="100", height="50"),
            direction="row",
            align="center",
            padding_x="10%",
            padding_y="20%"
        ),    

        rx.vstack( 
            rx.text(
                "Tendrás que descargar estas tres librerías desde la aplicación de Arduino. <TVout.h> , <video_gen.h>  y <fontALL.h>.",size="5"),
            rx.text(
                "Te dejo los esquemas del cableado. Si te gustan los proyectos en Arduino mírate el enlace que te dejo. De a hi saque la base de esto. Gracias.",size="5"),
            color="black",
            direction="column",
            spacing="2",
            justify="center",
            min_height="35vh",
        ),
        rx.hstack(
            rx.link(
                rx.button(rx.icon(tag="album"),"Arduinoinnovación",
                        color_scheme="red",
                        border_radius="2em",
                        box_sizing="border-box",
                        color="withe"),
                href="https://arduinovacao.blogspot.com/",
                is_external=True,
                size="5",
                weight="medium",
                trim="normal",
                padding_x="30%"
            ),
        ),    
        bg="#FFF3BC",
        position="sticky",
        align_items="start", 
        max_width="auto",
        padding_x="10px",
        padding_y="10px",
        flex_direction=["column","column","column","row","row"]
    )
    

app = rx.App()
app.add_page(index)
