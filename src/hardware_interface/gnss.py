from config import GPS_SERIAL_PORT, GPS_BAUD_RATE
from serial import Serial
from pyubx2 import UBXReader, NMEA_PROTOCOL, UBX_PROTOCOL

gps_serial = Serial(GPS_SERIAL_PORT, GPS_BAUD_RATE, timeout=1)
ubx_reader = UBXReader(
    gps_serial, protfilter=NMEA_PROTOCOL | UBX_PROTOCOL, readmode=1)


def get_state():
    gps_state = {}
    while True:
        data = ubx_reader.read()
        if data:
            if hasattr(data, 'lat') and data.lat:
                gps_state['lat'] = data.lat
            if hasattr(data, 'lon') and data.lon:
                gps_state['lon'] = data.lon
            if hasattr(data, 'heading') and data.heading:
                gps_state['heading'] = data.heading

            return gps_state
