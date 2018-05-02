from .common import InfoExtractor
import re
from ..utils import (
    js_to_json,
)


class NprmusicIE(InfoExtractor):
    _VALID_URL = r'(?:https?://)?(?:www\.)?npr\.org/event/music/(?P<id>\d{9})/(?P<name>.*)'
    # https://www.npr.org/event/music/533198237/tigers-jaw-tiny-desk-concert
    # _VALID_URL = r'(?:https?://)?(?:www\.)?vine\.co/v/(?P<id>\w+)'

    def _real_extract(self, url):
        print(str(type(url)))
        mobj = re.match(self._VALID_URL, url)

        video_id = mobj.group('id')
        video_url_name = mobj.group('name')

        webpage_url = 'https://npr.org/event/music/' + video_id + "/" + video_url_name
        webpage = self._download_webpage(webpage_url, video_id)

        # Log that we are starting to parse the page
        self.report_extraction(video_id)

        data = self._find_jwplayer_data(webpage)
        jwplayer_data = self._find_jwplayer_data(
            webpage, video_id, transform_source=js_to_json)
        print(data)

        # video_url = self._html_search_regex(r'<meta property="twitter:player:stream" content="(.+?)"', webpage, u'video URL')

        # video_url = self._html_search_regex(r'jwPlayer533201718', webpage, u'video URL')
        playerParams = r'jwPlayer533201718'

        pobj = re.match(playerParams, webpage)
        len(pobj)
        # paramsJson = pobj.group('json')
        #
        # print(paramsJson)

        return []
