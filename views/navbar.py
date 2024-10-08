import reflex as rx

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image("navbar.png",alt="tenis",width="32px",heigt="32px"),
            rx.text("PONG"),
            rx.spacer(),
            width="100%",
        )
    )