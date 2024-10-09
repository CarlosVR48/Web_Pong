import reflex as rx

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            #rx.color_mode.button(position="top-right"),
            rx.image("navbar.png",alt="tenis",width="32px",heigt="32px"),
            rx.text("PONG"),
            rx.spacer(),
            width="100%",
        ),
        bg="#1D2FFF",
        position="sticky",
        border_bottom="5px solid #FFFFFF",
        padding_x="25px",
        padding_y="25px",
        top="0",
        z_index="999",
        width="100%",
    )