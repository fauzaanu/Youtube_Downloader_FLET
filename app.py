import flet
from flet import Page, TextField, ElevatedButton, ProgressBar, Column, Text
from download import YoutubeDL

def main(page: Page):
    def download_event(e):
        download_url = link_text_input.value
        if ".be" in download_url or ".com" in download_url:
            page.clean()
            pb = ProgressBar(width=page.window_width / 3)


        page.add(
            Column([Text("Downloading..."), pb]),
        )
        download_object = YoutubeDL(download_url)
        if download_object.progress_amount == 100:
            page.clean()

            new_link_text_input = TextField(value="", label="Enter Youtube URL")
            new_download_button = ElevatedButton(text="Download", on_click=download_event)
            page.add(new_link_text_input, new_download_button)



    link_text_input = TextField(value="", label="Enter Youtube URL")
    download_button = ElevatedButton(text="Download", on_click=download_event)
    page.add(link_text_input, download_button)


flet.app(target=main, )
