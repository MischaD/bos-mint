from . import db


class LocalProposal(db.Model):
    """- **propsalIdentifier**: String, primaryKey
    - **reviewed**: Boolean, default=False

    Bos-mint uses Proposals to keep track of every element of any :data:`.utils.TYPENAMES`.
    Every propasal has an unique identifier and a reviewed variable that keeps   \
    track of whether a proposal has been reviewed or not.
    """
    proposelIdentifier = db.Column(db.String(128), primary_key=True)
    reviewed = db.Column(db.Boolean, default=False)

    @classmethod
    def getAllAsList(cls):
        """:returns: list of identifiers of all LocalProposals in the query
        """
        lpList = LocalProposal.query.all()
        return [x.proposelIdentifier for x in lpList]

    @classmethod
    def wasReviewed(cls, proposalId):
        """Checks whether a proposal with the given identifier exists and if it \
        doesn't we add one witch the id to the database and set it's reviewed \
        variable to True

        :param proposalId: Identifier of a proposal
        """
        lp = LocalProposal.query.get(proposalId)
        #TODO: why is reviewed only set to True when it doesnt exist already ??
        if lp is None:
            lp = LocalProposal(proposelIdentifier=proposalId, reviewed=True)
            db.session.add(lp)

        db.session.commit()


class ViewConfiguration(db.Model):
    """- **name**: String, primaryKey
    - **key**: String, primaryKey
    - **value**: String

    .. TODO: Understand this and explain it

    View Configuration for Bos-mint
    """
    name = db.Column(db.String(128), primary_key=True)
    key = db.Column(db.String(128), primary_key=True)
    value = db.Column(db.String(128))

    @classmethod
    def set(cls, name, key, value):
        """Set value of a View Configuration. If it doesn't exist already, a new one is created.

        :param name: Name of the view configuration (primary key)
        :param key: Key of the view configuration (primary key)
        :param value: Boolean or String that determines the value of a ViewConfiguration
        """
        if type(value) == bool:
            if value:
                value = 'True'
            else:
                value = 'False'

        # check if it exists
        vc = ViewConfiguration.query.filter_by(name=name, key=key).first()

        if vc is None:
            vc = ViewConfiguration(name=name, key=key, value=value)
            db.session.add(vc)
        else:
            vc.value = value

        db.session.commit()

    @classmethod
    def get(cls, name, key, default):
        """Get the value of a View Configuration with the given name and key.
        If a matching entry exist and the type of default is bool, type(return) \
        will be a bool as well. If none exist, it returns the default value.

        :param name: Name of the view configuration
        :param key: Key of the view configuration
        :param default: default value to be returned if no matching view configuration \
            exists
        :returns: Either the value of the entry or default
        """
        # check if it exists
        vc = ViewConfiguration.query.filter_by(name=name, key=key).first()

        if vc is None:
            return default
        else:
            if type(default) is bool:
                if vc.value == 'True':
                    return True
                else:
                    return False

            return vc.value
