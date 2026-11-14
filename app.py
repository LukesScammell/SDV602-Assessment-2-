
import argparse


def run_local():
    from local_gui import LocalGUI

    local_gui = LocalGUI()
    local_gui.run()


def run_remote():
    from chat_app import run

    run()


def main():
    parser = argparse.ArgumentParser(
        description="SDV602 Data Exploration System"
    )

    parser.add_argument(
        "mode",
        nargs="?",
        choices=["local", "remote"],
        default="local",
        help="Choose local or remote mode (default: local)"
    )

    args = parser.parse_args()

    if args.mode == "local":
        run_local()
    elif args.mode == "remote":
        run_remote()


if __name__ == "__main__":
    main()
