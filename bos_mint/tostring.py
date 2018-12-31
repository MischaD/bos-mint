# Global to string method for centralized visualization
from .istring import InternationalizedString


def findEnglishOrFirst(listOfIStrings, desiredLanguage='en'):
    """Returns the string of an entry in the list in a desired language. If the
    String is not available in your desired language, it returns the \
    first entry instead

    :param listOfIStrings: list of strings to be checked for the desired \
        language
    :param desiredLanguage: Language you are looking for, defualts to 'en'
    :returns: Internationalized String
    :rtype: str
    """
    return InternationalizedString.listToDict(listOfIStrings).get(
        desiredLanguage, listOfIStrings[0][1])


def toString(toBeFormatted, object=None):
    """.. TODO: Explain this and the whole module afterwards """
    if type(object).__name__ == "Event":
        if isinstance(toBeFormatted.get('name'), list):
            name = findEnglishOrFirst(toBeFormatted.get('name'))
        else:
            name = toBeFormatted.get('name')
        if name is None:
            displayName = "Unknown (deleted?)"
        else:
            displayName = name
        if toBeFormatted.get("start_time", None) is not None:
            displayName = str(toBeFormatted["start_time"]) + "Z" + ":\n" + displayName
        if toBeFormatted.get("id", None) is not None:
            displayName = displayName + ' (' + toBeFormatted['id'] + ')'
    elif toBeFormatted.get('name') and toBeFormatted.get('id'):
        if isinstance(toBeFormatted.get('name'), list):
            name = findEnglishOrFirst(toBeFormatted.get('name'))
        else:
            name = toBeFormatted.get('name')

        displayName = name + ' (' + toBeFormatted.get('id') + ')'
    elif toBeFormatted.get('description') and toBeFormatted.get('id'):
        if isinstance(toBeFormatted.get('description'), list):
            name = findEnglishOrFirst(toBeFormatted.get('description'))
        else:
            name = toBeFormatted.get('description')

        displayName = name + ' (' + toBeFormatted.get('id') + ')'
    elif toBeFormatted.get('id'):
        displayName = '(' + toBeFormatted.get('id') + ')'
        if object:
            displayName = object.__class__.__name__ + " " + displayName
    else:
        raise Exception

    if toBeFormatted.get('pendingOperationId'):
        displayName = displayName + '*(' +\
            toBeFormatted.get('pendingOperationId') + ')'

    return displayName
