from ai.recyclingClassification.recycling_predict import predict_recyclability
from ai.trashClassification.model_prediction import predict
from persistance.meldung_repository import MeldungRepository


class AppService:

    def __init__(self, link):
        self.__repository = MeldungRepository(link)

    def add_Meldung(self,meldung):
        meldung.category = float(predict(meldung.image))
        if meldung.category >= 50:
            meldung.recyclable = False
        else:
            meldung.recyclable = float(predict_recyclability(meldung.image))
        self.__repository.post_meldung_to_firebase(meldung)
