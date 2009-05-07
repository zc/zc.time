=======
zc.time
=======

zc.time provides a single point of creating datetime objects with the current
time.  It is easily swappable with a test method without having to monkeypatch
the standard datetime classes.

    >>> import zc.time
    >>> now = zc.time.now()
    >>> type(now)
    <type 'datetime.datetime'>

It also defaults to UTC, which the vanilla datetime does not.

    >>> now.tzinfo
    <UTC>
