from hardware_interface import gnss
from hardware_interface import communication
import time
import log

logger = log.getLogger(__name__)
logger.info("TelemetryCollector initialized.")


def collect_all_data(timeout=0.1, max_messages=10) -> dict:
    """Parses a raw sensor message and updates the global state dictionary."""
    collected_data = {}
    collected_data.update(gnss.get_state())

    return collected_data


# Example Usage (requires a mock or real SensorInterface and SerialCommunicator)
if __name__ == "__main__":
    from hardware_interface import communication
    from config import ROV_SERIAL_PORT

    if communication.is_connected():
        print(f"Mock communicator connected to {ROV_SERIAL_PORT}")

        print("\nCollecting telemetry data (attempt 1):")
        telemetry = collect_all_data()
        for key, value in telemetry.items():
            print(f"  {key}: {value}")

        print("\nCollecting telemetry data (attempt 2):")
        telemetry = collect_all_data()
        for key, value in telemetry.items():
            print(f"  {key}: {value}")

        communication.disconnect()
    else:
        print(
            f"Failed to connect communicator to {ROV_SERIAL_PORT}. Ensure serial port is running.")
