import reflex as rx
import datetime

def navbar() -> rx.Component:
    
    return rx.vstack(
        rx.hstack(
            #rx.color_mode.button(position="top-right"),
            rx.image("navbar.png",alt="tenis",width="32px",heigt="32px"),
            rx.text("PING-PONG"),
            rx.spacer(),
            rx.text(f"{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}"),
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