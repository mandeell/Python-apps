import time


def format_time(seconds):
    """Convert seconds to MM:SS format."""
    minutes, secs = divmod(seconds, 60)
    return f"{minutes:02d}:{secs:02d}"


def countdown_timer(seconds):
    """Run a simple countdown timer."""
    if seconds <= 0:
        print("Time must be greater than 0!")
        return

    print("Starting countdown...")
    while seconds > 0:
        print(f"\rTime remaining: {format_time(seconds)}", end='', flush=True)
        time.sleep(1)
        seconds -= 1

    print("\r⏰ Time's up!          ")


def main():
    """Get input and run the timer."""
    while True:
        try:
            user_input = input("Enter countdown time in seconds (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting timer...")
                break
            seconds = int(user_input)
            countdown_timer(seconds)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")


if __name__ == "__main__":
    main()