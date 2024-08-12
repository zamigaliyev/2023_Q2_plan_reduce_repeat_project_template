import os


def notify_admin(param):
    pass


def clean_logs(directory, threshold):
    # Get a list of log files in the directory
    log_files = get_log_files(directory)

    for log in log_files:
        # Check the size of the log file
        if log.size > threshold:
            # Clear the log if it exceeds the threshold
            clear_log(log)
            notify_admin("Log file {} was cleaned".format(log.name))


def get_log_files(directory):
    # Returns a list of log files in the given directory
    return os.listdir(directory)


def clear_log(log):
    # Clears the content of the log file
    with open(log, 'w'):
        pass


# Example usage
clean_logs('/var/logs', 100 * 1024 * 1024)  # Clean logs over 100MB
