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
            rx.heading("🔵 Crea tu propia máquina", size="8"),
            justify="center",
            min_height="25vh",
            padding_y="10px",
        ),
        rx.vstack(    
            rx.image(src="pong_01.png",alt="Maquina de pong Arduino UNO",width="370px", height="230px"),
            rx.image(src="pong_02.png",alt="Maquina de pong Arduino UNO",width="370px", height="230px"),
            spacing="3",
            min_height="35vh",
            padding_x="30%",
            position="sticky"
        ),
        rx.vstack( 
            rx.text(
                "El proyecto ha sido construido con el Arduino Uno. Conexión RCA de línea de video y de sonido. Interruptor para seleccionar 2 modalidades de juego.", size="5"),
            rx.text(
                "El repositorio del programa de pong del Arduino UNO, se encuentra en el enlace de gitHub de más abajo", size="5"),
            direction="column",
            spacing="5",
            justify="center",
            min_height="30vh"
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
            min_height="45vh"
        ),
        rx.hstack(
            rx.link(
                rx.button("Enlace de gitHub"),
                href="https://github.com/carlosvr48",
                is_external=True,
                color="red",
                size="5",
                weight="medium",
                trim="normal"
            ),        
            rx.image(src="github.png",alt="gitHub",width="64", height="25"),
            direction="row",
            align="center",
            padding_x="30%",

        ),
        rx.vstack( 
            rx.text("Intenta representar la maravillosa máquina de videojuegos de Atari Pong. La primera máquina se llamó Tele-Games Pong (1975) y la segunda Atari Pong (1976). En el siguiente enlace de la wiki dejo un poco de historia.",size="5"),
            direction="column",
            justify="center",
            min_height="35vh"
        ),       
        rx.hstack(     
            rx.link(
                rx.button("Wikipedia"),
                href="https://es.wikipedia.org/wiki/Atari_Pong",
                is_external=True,
                size="5",
                weight="medium",
                trim="normal"
            ),
            rx.image(src="pong1.png",alt="Maquina de pong Atari",width="100", height="50"),
            direction="row",
            align="center",
            padding_x="30%",
        ),    
        rx.vstack( 
            rx.text(
                "Tendrás que descargar estas tres librerías desde la aplicación de Arduino. <TVout.h> , <video_gen.h>  y <fontALL.h>.",size="5"),
            rx.text(
                "Te dejo los esquemas del cableado. Si te gustan los proyectos en Arduino mírate el enlace que te dejo. De a hi saque la base de esto. Gracias",size="5"),
            direction="column",
            spacing="2",
            justify="center",
            min_height="35vh",
        ),
        rx.hstack(
            rx.link(
                rx.button("Enlace de Arduinoinnovación"),
                href="https://arduinovacao.blogspot.com/",
                is_external=True,
                size="5",
                weight="medium",
                trim="normal",
            ),padding_x="30%"
        ),    
        align_items="start", 
        max_width="1200px",
        padding_x="10px",
        padding_y="10px",
        bg="#FFF3BC",
        flex_direction=["column","column","column","row","row"]
    )

app = rx.App()
app.add_page(index)
