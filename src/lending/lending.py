class Lending:
    def __init__(self, lender, borrower, media):
        self.__lender = lender
        self.__borrower = borrower
        self.__media = media
        #lenddate?
        #returndate?

@property
def lender(self):
    return self.__lender

@property
def borrower(self):
    return self.__borrower

@property
def media(self):
    return self.__media

def to_dict():
    return {
            "type" : "Lending",
            "lender" : self.__lender,
            "borrower" : self.__borrower,
            "media" : self.__media
    }

    