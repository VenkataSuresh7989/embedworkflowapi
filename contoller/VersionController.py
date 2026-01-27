from view import VersionView


def getallversioninfo():
    return VersionView.getallversioninfo()


def createmodule(data):
    return VersionView.createmodule(data)


def updatemodule(id, data):
    return VersionView.updatemodule(id, data)


def deletemodule(id):
    return VersionView.deletemodule(id)


def createfw(data):
    return VersionView.createfw(data)


def updatefw(id, data):
    return VersionView.updatefw(id, data)


def deletefw(id):
    return VersionView.deletefw(id)