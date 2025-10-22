from config import ROV_I2C_BUS, ROV_I2C_ADDRESS, ROV_I2C_REGISTER
from smbus2 import SMBus
import log

logger = log.getLogger(__name__)
i2c = SMBus(ROV_I2C_BUS)

motor_state = [1500, 1500, 1500, 1500]  # Neutral speeds for 4 motors


def set_motor_speed(motor_id: int, speed: int) -> bool:
    """
    Sets the speed of a specific motor.
    """
    global motor_state
    try:
        motor_state[motor_id] = speed
        i2c.write_block_data(
            ROV_I2C_ADDRESS,
            ROV_I2C_REGISTER,
            bytes(','.join(map(str, motor_state)), 'utf-8')
        )
        return True
    except Exception as e:
        logger.error(f"Failed to set motor {motor_id} speed to {speed}: {e}")
        return False


def stop_all_motors() -> bool:
    """
    Stops all motors.
    This might involve sending individual stop commands or a global stop command.
    """
    global motor_state
    try:
        motor_state = [1500, 1500, 1500, 1500]  # Reset to neutral speeds
        i2c.write_block_data(
            ROV_I2C_ADDRESS,
            ROV_I2C_REGISTER,
            bytes(','.join(map(str, motor_state)), 'utf-8')
        )
        return True
    except Exception as e:
        logger.error(f"Failed to stop all motors: {e}")
        return False


def set_thruster_speeds(speeds: list[int]) -> bool:
    """
    Sets speeds for multiple thrusters at once.
    Args:
        speeds (list[int]): A list of speeds, one for each thruster.
                            The order should match your ROV's thruster configuration.
    Returns:
        bool: True if all commands were likely sent successfully, False otherwise.
    """
    global motor_state
    if len(speeds) != len(motor_state):
        logger.error(f"Expected {len(motor_state)} speeds, got {len(speeds)}.")
        return False

    try:
        motor_state = speeds
        i2c.write_block_data(
            ROV_I2C_ADDRESS,
            ROV_I2C_REGISTER,
            bytes(','.join(map(str, motor_state)), 'utf-8')
        )
        return True
    except Exception as e:
        logger.error(f"Failed to set thruster speeds {speeds}: {e}")
        return False


# Example Usage (if you were to test motors.py directly)
if __name__ == "__main__":
    logger.info("Setting motor 0 speed to 1600")
    set_motor_speed(0, 1600)

    logger.info("Setting all thruster speeds to [1600, 1400, 1500, 1500]")
    set_thruster_speeds([1600, 1400, 1500, 1500])

    logger.info("Stopping all motors")
    stop_all_motors()
