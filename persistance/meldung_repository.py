import json

import requests

from domain.meldung import Meldung


class MeldungRepository:
    def __init__(self, link_to_firebase):
        self.link_to_firebase = link_to_firebase

    def post_meldung_to_firebase(self, meldungVar):
        requests.post(url=self.link_to_firebase, json=meldungVar.to_json())


if __name__ == '__main__':
    # Testing
    repo = MeldungRepository('https://get-wasted-db-default-rtdb.firebaseio.com/Meldungen.json')
    meldung = Meldung(2, 2, 2, 2, 2, 6)
    repo.post_meldung_to_firebase(meldung)
