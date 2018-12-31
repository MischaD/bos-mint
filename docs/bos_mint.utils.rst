bos\_mint\.utils module
=======================

.. TODO what does this module do ?

Additionally utils saves a bunch of dictionaries with useful data about the different \
typenames, it's parent/child relationships, identifiers and available operations, namely:

- TYPENAMES: All typenames available in Peerplays
- TYPE_GET_ALL: get list of objects for typename, containing id, \
    and toString field
- TYPE_GET: get list of objects for typename, containing id and toString field
- PARENTTYPE_GET: get object for typename and containing id of parent object
- CHILD_TYPE: which type does one type cascade to
- PARENT_TYPE: from which type does one type come from
- OP_TO_TYPENAME_MAP: Maps all available operation to the corresponding \
    typename


.. automodule:: bos_mint.utils
    :members:
    :undoc-members:
    :show-inheritance:
