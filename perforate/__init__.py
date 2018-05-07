from datetime import datetime
import zlib

import zmq

from .perforate_pb2 import EventClass, Metric, Event, Measurement, Message


#TODO: needs thread safety
class Perforate(object):
    def __init__(self, host='127.0.0.1', port=14541, session_renewal_interval=5):
        context = zmq.Context.instance()
        self.socket = context.socket(zmq.PUB)
        self.socket.connect('tcp://%s:%d'%(host,port))
        self.event_classes = {}
        self.metrics = {}
        self._session_renewal_interval = session_renewal_interval
        self._hashes_used = set()

    def _send_message(self, **kwargs):
        self.socket.send(Message(**kwargs).SerializeToString())
        

    def _with_redeclaration(self, **kwargs):
        def _(fn):
            last_declared = datetime.now()
            def wrapped(*wargs, **wkwargs):
                nonlocal last_declared
                now = datetime.now()
                if (now - last_declared).seconds > self._session_renewal_interval:
                    self._send_message(**kwargs)
                    last_declared = now
                fn(*wargs, **wkwargs)
            return wrapped
        return _

    def _make_session_code(self, value):
        h = zlib.crc32(bytes(value, 'ascii'))
        while h in self._hashes_used:
            h = h + 1
        self._hashes_used.add(h)
        return h
    
    def register_event_class(self, label, name, is_prolonged):
        assert label not in self.event_classes
        session_code = self._make_session_code(label)
        self.event_classes[label] = session_code       
        ec = EventClass(
            label=label,
            name=name,
            is_prolonged=is_prolonged,
            session_code=session_code
        )
        self._send_message(eventclass=ec)

        @self._with_redeclaration(eventclass=ec)
        def emit_this_event(value=None, duration=None):
            self._emit_event(session_code, value=value, duration=duration)
        setattr(self, 'emit_%s'%label, emit_this_event)
        
    def register_metric(self, label, name):
        assert label not in self.metrics
        session_code = self._make_session_code(label)
        self.metrics[label] = session_code
        m = Metric(
            label=label,
            name=name,
            session_code=session_code)

        self._send_message(metric=m)

        @self._with_redeclaration(metric=m)
        def record_this_metric(value):
            self._record_measurement(session_code, value)
        setattr(self, 'record_%s'%label, record_this_metric)
        
        

    def _emit_event(self, session_code, value=None, duration=None):
        ev = Event(
            class_session_code = session_code,
            value = value)
        if duration is not None:
            ev.duration = duration
        self._send_message(event=ev)

            
    def _record_measurement(self, session_code, value):
        m = Measurement(
            metric_session_code=session_code,
            value=value)
        self._send_message(measurement=m)

        
