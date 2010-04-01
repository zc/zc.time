import datetime
import pytz


def now():
    if _t:
        return _t
    else:
        return datetime.datetime.now(pytz.UTC)


_now = now
_t = None


def utcnow():
    return now().replace(tzinfo=None)


def set_now(t):
    global _t
    tz = t.tzinfo
    if tz is None:
        t = pytz.UTC.localize(t)
    elif tz is not pytz.UTC:
        t = t.astimezone(pytz.UTC)
    _t = t


def reset():
    global now, _t
    now = _now
    _t = None


# Play the conditional import game to avoid a required dependency.
try:
    import zope.testing.cleanup
except ImportError:
    pass
else:
    zope.testing.cleanup.addCleanUp(reset)
