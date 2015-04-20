=======
zc.time
=======

zc.time provides a single point of creating datetime objects with the current
time.  It is easily swappable with a test method without having to monkeypatch
the standard datetime classes.

    >>> import time
    >>> import zc.time

    >>> now = zc.time.now()

    >>> type(now)
    <type 'datetime.datetime'>

It also defaults to UTC, which the vanilla datetime does not.

    >>> now.tzinfo
    <UTC>

There's also a ``utcnow()`` function, which returns the naive UTC time
corresponding to the ``now()`` function's return value.  This provides a
utcnow() implementation that's similarly affected by replacing the
``now()`` function:

    >>> now = zc.time.utcnow()

    >>> type(now)
    <type 'datetime.datetime'>

    >>> now.tzinfo

This relationship holds even if ``now()`` is replaced (not recommended):

    >>> import datetime
    >>> import pytz

    >>> t = datetime.datetime(2010, 4, 1, 10, 50, 30, 2345, pytz.UTC)
    >>> old_now = zc.time.now

    >>> zc.time.now = lambda: t

    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 10, 50, 30, 2345, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 10, 50, 30, 2345)

The ``reset()`` function provided cleans up modifications made to
control the time:

    >>> zc.time.reset()
    >>> zc.time.now is old_now
    True

A ``set_now()`` function is provided that takes a datetime, and causes
``now()`` and ``utcnow()`` to pretend that's the real time.  The time
passed in can be in any time zone; naive times are converted to UTC
using ``pytz.UTC.localize``:

    >>> zc.time.set_now(t)

    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 10, 50, 30, 2345, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 10, 50, 30, 2345)
    >>> time.time()
    1270137030.002345

    >>> naive = datetime.datetime(2010, 4, 1, 12, 27, 3, 5432)

    >>> zc.time.set_now(naive)

    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 12, 27, 3, 5432, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 12, 27, 3, 5432)
    >>> time.time()
    1270142823.005432

    >>> t = datetime.datetime(2010, 4, 1, 11, 17, 3, 5432,
    ...                       pytz.timezone("US/Eastern"))

    >>> zc.time.set_now(t)

    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 16, 17, 3, 5432, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 16, 17, 3, 5432)
    >>> time.time()
    1270156623.005432

To move forward in time, simply use ``set_now()`` again:

    >>> zc.time.set_now(t + datetime.timedelta(hours=1))

    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 17, 17, 3, 5432, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 17, 17, 3, 5432)
    >>> time.time()
    1270160223.005432

If an application sleeps using ``time.sleep``, that'll be reflected in
the times reported:

    >>> import time

    >>> time.sleep(0.25)
    >>> zc.time.now()
    datetime.datetime(2010, 4, 1, 17, 17, 3, 255432, tzinfo=<UTC>)
    >>> zc.time.utcnow()
    datetime.datetime(2010, 4, 1, 17, 17, 3, 255432)
    >>> time.time()
    1270160223.255432

The reported time will be updated by the exact delay requested of the
``time.sleep`` call, rather than by the actual delay.

The ``reset()`` function is used to clean up after this as well:

    >>> zc.time.reset()

The ``reset()`` is registered as a general cleanup handler if
``zope.testing`` is available.  This is generally not sufficient for
functional tests, which will need to call ``reset`` themselves.


Changes
=======


1.0.1 (2015-04-20)
------------------

- Fix packaging bug.


1.0.0 (2015-04-20)
------------------

- Include ``time.time`` in what's controlled by ``zc.time.set_now``.


0.3 (2010-07-23)
----------------

- Added time.sleep() support.


0.2 (2010-04-01)
----------------

- Added utcnow().
- Added set_now(), reset().


0.1
---

Initial release.
