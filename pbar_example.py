from time import sleep

import flet
from flet import Column, Page, ProgressBar, Text

def main(page: Page):
    pb = ProgressBar(width=page.window_width/3,)

    page.add(
        Text("Downloading", style="headlineSmall"),
        Column([Text("Doing something..."), pb]),
    )

    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(0.1)
        page.update()

flet.app(target=main)