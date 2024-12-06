from pytz import timezone
import reflex as rx
import datetime,time

def navbar() -> rx.Component:
    dia_españa = datetime.datetime.now(timezone("Europe/Madrid"))
    final_españa = datetime.datetime.strftime(dia_españa,"%d-%m-%Y %H:%M:%S ")

    return rx.vstack(

        rx.hstack(
            #rx.color_mode.button(position="top-right"),
            rx.image("navbar.png",alt="tenis",width="32px",heigt="32px"),
            rx.text(f"PING-PONG"),
            rx.spacer(),
            rx.text(f"{final_españa}"),
            color="black",
            width="100%"
        ),
        bg="#FFF3BC",
        position="sticky",
        border_bottom="2px solid #000000",
        padding_x="25px",
        padding_y="15px",
        top="0",
        z_index="999",
        width="100%",
        
    )