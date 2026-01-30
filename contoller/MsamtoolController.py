from view import MsamtoolView

def createtoolheaders(headername):
    return MsamtoolView.createtoolheaders(headername)

def updatetoolheaders(header_id, headername):
    return MsamtoolView.updatetoolheaders(header_id, headername)

def deletetoolheader(header_id):
    return MsamtoolView.deletetoolheader(header_id)


def createtoolheaderItems(data):
    return MsamtoolView.createtoolheaderItems(data)

def updatetoolheaderItems(header_id, data):
    return MsamtoolView.updatetoolheaderItems(header_id, data)

def deletetoolheaderItems(header_id):
    return MsamtoolView.deletetoolheaderItems(header_id)


def get_tool_headers_with_items():
    return MsamtoolView.get_tool_headers_with_items()









