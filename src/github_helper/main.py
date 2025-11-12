import argparse


def parse_arguments(args=None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    Args:
        args: List of arguments to parse. If None, uses sys.argv[1:]
    """
    parser = argparse.ArgumentParser(
        description='GitHub helper utility',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example: python -m src.github_helper.main -o abc -v'
    )
    # Required argument
    parser.add_argument(
        "-o", "--operation",
        type=str,
        choices=["any", "none"],
        required=True,
        help="Choose something"
    )
    # Optional argument
    parser.add_argument(
        "-f", "--file",
        type=str,
        default="/tmp/something.tmp",
        help="Choose file"
    )
    return parser.parse_args(args)


def main():
    print('Hello world')


if __name__ == "__main__":
    main()
