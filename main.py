import webbrowser

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.event import ItemEnterEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

class BingSearchExtension(Extension):
    def __init__(self):
        super(BingSearchExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or ""
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name='Search Bing for "{}"'.format(query),
                description='Press Enter to search Bing',
                on_enter=OpenUrlAction(f'https://www.bing.com/chat?q={query}&qs=ds&form=CONVCP')
            )
        ])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or ""
        url = f'https://www.bing.com/chat?q={query}&qs=ds&form=CONVCP'
        webbrowser.open(url)

if __name__ == '__main__':
    BingSearchExtension().run()
