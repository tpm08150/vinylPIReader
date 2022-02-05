import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from spotipy.oauth2 import SpotifyOAuth
import discogs_client
import time

d = discogs_client.Client(
    'my_user_agent/1.0',
    consumer_key='PgginxHnQACcRgdwJOts',
    consumer_secret='nAIHrbAmCnSJbqXEfkTDXXsmGLdltrRG',
    token=u'DMlaoFlUojEZysbdieNgIJnrJlFcgbkFfloTvSPc',
    secret=u'TAWweIrwFrcFLouGKUaempCDeYLzetHsbmAeMkub'
)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="b76becc6c4d24b8696897f19089eaf10",
                                               client_secret="d1e9c909581243bd9785f3e77991d8b0",
                                               redirect_uri="http://google.com/",
                                               scope="user-library-read"))
barcode = ['07464368441']
results = d.search(barcode[0], type='release')
artist = results[0].artists[0]
album = results[0]

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        global album_artist
        global album_art
        global album_title
        global artist
        global results
        global search
        global img

        super(MyGridLayout, self).__init__(**kwargs)

        search = sp.search(album.title + ' ' + album.tracklist[0].title, limit=1, offset=0, type='track', market=None)
        print(search)
        album_art = search['tracks']['items'][0]['album']['images'][0]['url']
        album_artist = search['tracks']['items'][0]['album']['artists'][0]['name']
        album_title = search['tracks']['items'][0]['album']['name']
        print(album_artist)
        print(album_title)

        self.cols = 3
        self.albumArt = AsyncImage(source=album_art)
        self.add_widget(self.albumArt)

        self.artistLabel = Label(text=str(album_artist))
        self.add_widget(self.artistLabel)

        self.albumLabel = Label(text=str(album_title))
        self.add_widget(self.albumLabel)

        self.barcode = TextInput(multiline=False)
        self.add_widget(self.barcode)

        self.enterButton = Button(text='enter', background_color='gray', background_normal='', size_hint=(.3, .1))
        self.add_widget(self.enterButton)
        self.enterButton.bind(on_press=self.enter)


    def enter(self, instance):
        global album_artist
        global album_art
        global album_title
        global artist
        global results
        global album
        global search
        global img

        print(self.barcode.text)
        barcode.insert(0, str(self.barcode.text))
        barcode.pop(1)
        print(barcode)
        results = d.search(barcode[0], type='release')
        album = results[0]
        print(album.title)
        print(album.tracklist[0].title)
        time.sleep(0.1)
        search = sp.search(album.title + ' ' + album.tracklist[0].title, limit=1, offset=0, type='track', market=None)
        album_art = search['tracks']['items'][0]['album']['images'][0]['url']
        album_artist = search['tracks']['items'][0]['album']['artists'][0]['name']
        album_title = search['tracks']['items'][0]['album']['name']

        self.artistLabel.text = str(album_artist)
        self.albumLabel.text = str(album_title)
        self.albumArt.source = album_art

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
        MyApp().run()